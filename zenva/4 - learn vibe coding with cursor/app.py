import uuid
from pathlib import Path

from flask import Flask, render_template, request, send_from_directory, url_for
from PIL import Image
from werkzeug.utils import secure_filename

APP_NAME = "ZenvaResizer"
BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
ALLOWED_EXTENSIONS = {".png", ".jpg", ".jpeg"}
MAX_FILES = 5

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


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    error = None
    form_values = {"width": "800", "height": "600", "quality": "85"}

    if request.method == "POST":
        files = request.files.getlist("images")
        width = parse_positive_int(request.form.get("width"), 800)
        height = parse_positive_int(request.form.get("height"), 600)
        quality = parse_positive_int(request.form.get("quality"), 85)
        quality = max(1, min(quality, 95))

        form_values = {
            "width": str(width),
            "height": str(height),
            "quality": str(quality),
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
    )


@app.route("/uploads/<path:filename>")
def uploaded_file(filename: str):
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=False)


@app.route("/download/<path:filename>")
def download_file(filename: str):
    return send_from_directory(UPLOAD_DIR, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
