# ZenvaResizer

Minimal Flask web app to batch-resize images with Pillow.

## Features

- Upload up to 5 images at once
- Accepted formats (by extension): `PNG`, `JPG`, `JPEG`
- Set target `width`, `height`, and `quality`
- Optional horizontal mirror effect
- Preview resized images in browser
- Download resized images one by one
- Processed files served from temporary `uploads/` using Flask `send_from_directory`

## Tech Stack

- Python
- Flask
- Pillow
- Jinja2 templates + basic CSS (neon style)

## Project Structure

```text
.
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Setup

1. Create and activate a virtual environment (recommended):

   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .\.venv\Scripts\Activate.ps1
     ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open in browser:

   - [http://127.0.0.1:5000](http://127.0.0.1:5000)

## How To Use

1. Choose up to 5 image files.
2. Enter width, height, and quality.
3. Optionally enable **Mirror output horizontally**.
4. Click **Resize Images**.
5. Preview results and download each image.

## Notes

- This is a minimal app by design.
- File validation currently checks extension only.
- No authentication, CSRF protection, or header hardening included.
