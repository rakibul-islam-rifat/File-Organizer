import logging
from pathlib import Path
from shutil import move

logger: logging.Logger = logging.getLogger(__name__)

Home_folder: Path = Path(__file__).parent / "HOME"
Home_folder.mkdir(parents=True, exist_ok=True)

subfolder_names: dict[str, str] = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".pdf": "PDFs",
    ".txt": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".mp4": "Videos",
    ".mov": "Videos",
}


def subfolder_constructor(extension: str) -> Path:
    subfolder_name: str = subfolder_names.get(extension, "Others")
    subfolder: Path = Home_folder / subfolder_name
    subfolder.mkdir(exist_ok=True, parents=True)
    logger.debug("Created Sub-Folder: %s", subfolder.name)
    return subfolder


def filename_checker(subfolder: Path, filename: str, extension: str) -> Path:
    file: Path = subfolder / f"{filename}{extension}"
    i = 1
    while file.is_file():
        logger.debug("File name: %s exists in the Sub-Folder: %s", filename, subfolder)
        file = subfolder / f"{filename}_{i:03}{extension}"
        i += 1

    return file


def move_all(target: str) -> None:
    target_folder: Path = Path(target)
    if not Path(target).exists():
        logger.error("Folder '%s' does not exist.", target)
        return

    for file in target_folder.iterdir():
        if not file.is_file():
            continue

        filename: str = file.stem
        extension: str = file.suffix
        subfolder: Path = subfolder_constructor(extension)
        new_file: Path = filename_checker(subfolder, filename, extension)
        move(file.resolve(), new_file)
        logger.info("Moved %s to %s", file.name, str(new_file))
