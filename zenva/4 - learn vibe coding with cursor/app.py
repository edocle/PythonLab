import uuid
from pathlib import Path

from flask import Flask, render_template, request, send_from_directory, url_for
from PIL import Image, ImageColor, ImageDraw, ImageFont, ImageOps
from werkzeug.utils import secure_filename

APP_NAME = "ZenvaResizer"
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}
MAX_FILES = 5
WATERMARK_POSITIONS = {
    "top-left",
    "top-right",
    "center",
    "bottom-left",
    "bottom-right",
}
WATERMARK_FONT_CHOICES = ["Roboto", "Montserrat", "Orbitron"]
WATERMARK_FONT_FILES = {
    "Roboto": "DejaVuSans.ttf",
    "Montserrat": "DejaVuSans.ttf",
    "Orbitron": "DejaVuSans-Bold.ttf",
}

app = Flask(__name__)
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def allowed_file(filename: str) -> bool:
    return Path(filename).suffix.lower() in ALLOWED_EXTENSIONS


def parse_positive_int(value: str, fallback: int) -> int:
    try:
        parsed = int(value)
        return parsed if parsed > 0 else fallback
    except (TypeError, ValueError):
        return fallback


def parse_int_with_bounds(value: str, fallback: int, minimum: int, maximum: int) -> int:
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return fallback
    return max(minimum, min(parsed, maximum))


def parse_color(value: str, fallback: str) -> str:
    try:
        ImageColor.getrgb(value)
        return value
    except ValueError:
        return fallback


def calculate_position(canvas_size, item_size, position: str, margin: int):
    canvas_w, canvas_h = canvas_size
    item_w, item_h = item_size

    if position == "top-left":
        return margin, margin
    if position == "top-right":
        return max(margin, canvas_w - item_w - margin), margin
    if position == "center":
        return max(0, (canvas_w - item_w) // 2), max(0, (canvas_h - item_h) // 2)
    if position == "bottom-left":
        return margin, max(margin, canvas_h - item_h - margin)
    return max(margin, canvas_w - item_w - margin), max(margin, canvas_h - item_h - margin)


def get_watermark_font(font_family: str, font_size: int):
    filename = WATERMARK_FONT_FILES.get(font_family, "DejaVuSans.ttf")
    try:
        return ImageFont.truetype(filename, font_size)
    except OSError:
        return ImageFont.load_default()


def apply_text_watermark(image: Image.Image, settings: dict) -> Image.Image:
    base = image.convert("RGBA")
    text = settings["text"]
    opacity = settings["opacity"]
    position = settings["position"]
    margin = settings["margin"]
    rotation = settings["rotation"]
    stroke_width = settings["stroke_width"]

    font_size = settings["font_size"] or max(14, base.width // 24)
    font = get_watermark_font(settings["font_family"], font_size)
    fill_rgb = ImageColor.getrgb(settings["color"])
    stroke_rgb = ImageColor.getrgb(settings["stroke_color"])
    fill_rgba = (fill_rgb[0], fill_rgb[1], fill_rgb[2], int(255 * (opacity / 100)))
    stroke_rgba = (
        stroke_rgb[0],
        stroke_rgb[1],
        stroke_rgb[2],
        int(255 * (opacity / 100)),
    )

    measure_draw = ImageDraw.Draw(Image.new("RGBA", (1, 1), (0, 0, 0, 0)))
    bbox = measure_draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    text_w = max(1, bbox[2] - bbox[0])
    text_h = max(1, bbox[3] - bbox[1])

    text_layer = Image.new("RGBA", (text_w + 6, text_h + 6), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_layer)
    text_draw.text(
        (3 - bbox[0], 3 - bbox[1]),
        text,
        font=font,
        fill=fill_rgba,
        stroke_width=stroke_width,
        stroke_fill=stroke_rgba,
    )

    if rotation != 0:
        resample = getattr(Image, "Resampling", Image).BICUBIC
        text_layer = text_layer.rotate(rotation, expand=True, resample=resample)

    x, y = calculate_position(base.size, text_layer.size, position, margin)
    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    overlay.paste(text_layer, (x, y), text_layer)
    return Image.alpha_composite(base, overlay)


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    error = None
    form_values = {
        "width": "800",
        "height": "600",
        "quality": "85",
        "mirror": False,
        "watermark_enabled": False,
        "watermark_text": "edocle",
        "watermark_position": "bottom-right",
        "watermark_opacity": "35",
        "watermark_font_size": "",
        "watermark_font_family": "Roboto",
        "watermark_color": "#FFFFFF",
        "watermark_margin": "12",
        "watermark_rotation": "0",
        "watermark_stroke_color": "#000000",
        "watermark_stroke_width": "2",
    }

    if request.method == "POST":
        files = request.files.getlist("images")
        width = parse_positive_int(request.form.get("width"), 800)
        height = parse_positive_int(request.form.get("height"), 600)
        quality = parse_positive_int(request.form.get("quality"), 85)
        quality = max(1, min(quality, 95))
        mirror = request.form.get("mirror") == "on"
        watermark_enabled = request.form.get("watermark_enabled") == "on"
        watermark_text = (request.form.get("watermark_text") or "edocle").strip()[:80] or "edocle"
        watermark_position = request.form.get("watermark_position", "bottom-right")
        if watermark_position not in WATERMARK_POSITIONS:
            watermark_position = "bottom-right"
        watermark_opacity = parse_int_with_bounds(
            request.form.get("watermark_opacity"), 35, 0, 100
        )
        watermark_font_size = parse_int_with_bounds(
            request.form.get("watermark_font_size"), 0, 0, 512
        )
        watermark_font_family = request.form.get("watermark_font_family", "Roboto")
        if watermark_font_family not in WATERMARK_FONT_CHOICES:
            watermark_font_family = "Roboto"
        watermark_color = parse_color(request.form.get("watermark_color"), "#FFFFFF")
        watermark_margin = parse_int_with_bounds(request.form.get("watermark_margin"), 12, 0, 500)
        watermark_rotation = parse_int_with_bounds(
            request.form.get("watermark_rotation"), 0, -360, 360
        )
        watermark_stroke_color = parse_color(request.form.get("watermark_stroke_color"), "#000000")
        watermark_stroke_width = parse_int_with_bounds(
            request.form.get("watermark_stroke_width"), 2, 0, 32
        )

        form_values = {
            "width": str(width),
            "height": str(height),
            "quality": str(quality),
            "mirror": mirror,
            "watermark_enabled": watermark_enabled,
            "watermark_text": watermark_text,
            "watermark_position": watermark_position,
            "watermark_opacity": str(watermark_opacity),
            "watermark_font_size": str(watermark_font_size) if watermark_font_size > 0 else "",
            "watermark_font_family": watermark_font_family,
            "watermark_color": watermark_color,
            "watermark_margin": str(watermark_margin),
            "watermark_rotation": str(watermark_rotation),
            "watermark_stroke_color": watermark_stroke_color,
            "watermark_stroke_width": str(watermark_stroke_width),
        }

        selected_files = [f for f in files if f and f.filename]
        if not selected_files:
            error = "Please upload at least one image."
        elif len(selected_files) > MAX_FILES:
            error = f"You can upload up to {MAX_FILES} images only."
        else:
            for uploaded_file in selected_files:
                original_name = secure_filename(uploaded_file.filename)
                if not original_name or not allowed_file(original_name):
                    continue

                extension = Path(original_name).suffix.lower()
                token = uuid.uuid4().hex
                saved_name = f"{Path(original_name).stem}_{token}{extension}"
                output_path = UPLOAD_DIR / saved_name

                with Image.open(uploaded_file.stream) as img:
                    resized = img.resize((width, height))
                    if mirror:
                        resized = ImageOps.mirror(resized)
                    if watermark_enabled:
                        resized = apply_text_watermark(
                            resized,
                            {
                                "text": watermark_text,
                                "position": watermark_position,
                                "opacity": watermark_opacity,
                                "font_size": watermark_font_size,
                                "font_family": watermark_font_family,
                                "color": watermark_color,
                                "margin": watermark_margin,
                                "rotation": watermark_rotation,
                                "stroke_color": watermark_stroke_color,
                                "stroke_width": watermark_stroke_width,
                            },
                        )
                    if extension in {".jpg", ".jpeg"}:
                        if resized.mode in ("RGBA", "P"):
                            resized = resized.convert("RGB")
                        resized.save(output_path, quality=quality, optimize=True)
                    else:
                        resized.save(output_path, optimize=True)

                results.append(
                    {
                        "original_name": original_name,
                        "saved_name": saved_name,
                        "preview_url": url_for("uploaded_file", filename=saved_name),
                        "download_url": url_for("download_file", filename=saved_name),
                    }
                )

            if not results and error is None:
                error = "No valid image files found. Use PNG, JPG, or JPEG."

    return render_template(
        "index.html",
        app_name=APP_NAME,
        results=results,
        error=error,
        max_files=MAX_FILES,
        form_values=form_values,
        watermark_font_choices=WATERMARK_FONT_CHOICES,
    )


@app.route("/uploads/<path:filename>")
def uploaded_file(filename: str):
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=False)


@app.route("/download/<path:filename>")
def download_file(filename: str):
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
