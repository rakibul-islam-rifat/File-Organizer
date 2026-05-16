# File Organizer

A Python automation tool that organizes a messy folder by sorting files into subfolders based on their file type.

## What It Does

- Takes a target folder name as input
- Scans all files in that folder
- Moves each file into a subfolder based on its extension (Images, PDFs, Documents, Videos, Others)
- Creates subfolders automatically if they don't exist
- Handles duplicate filenames by appending a number (e.g. `report_001.pdf`)
- Logs every move and error

## Project Structure

```
file-organizer/
├── HOME/                  # organized output folder (created automatically)
├── organizer.py           # core logic — scanning, moving, duplicate handling
├── main.py                # entry point, takes folder name as input
├── logger_setup.py        # rotating file + console logging
└── requirements.txt
```

## Setup

**1. Clone the repo and install dependencies:**
```bash
git clone https://github.com/rakibul-islam-rifat/file-organizer
cd file-organizer
uv pip install -r requirements.txt
```

**2. Place the folder you want to organize inside the project directory, then run:**
```bash
python main.py
```

## Output

Files are moved into `HOME/` with subfolders:
- **Images** — `.jpg`, `.jpeg`, `.png`
- **PDFs** — `.pdf`
- **Documents** — `.txt`, `.doc`, `.docx`
- **Videos** — `.mp4`, `.mov`
- **Others** — anything else

## Dependencies

- `pathlib` — directory traversal and path handling (standard library)
- `shutil` — file moving (standard library)
- `logging` — rotating log file + console output (standard library)