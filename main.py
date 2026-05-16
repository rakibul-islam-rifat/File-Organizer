import logging

from logger_setup import setup_logging
from organizer import move_all

setup_logging("organizer.log")
logger: logging.Logger = logging.getLogger(__name__)


def main() -> None:
    print("Place the Folder you wanna organize in the current folder")
    target: str = input("What is the name of the folder: ")
    move_all(target=target)


if __name__ == "__main__":
    main()
