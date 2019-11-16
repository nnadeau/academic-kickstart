import subprocess
import datetime
import logging
from pathlib import Path
from string import ascii_lowercase, digits, printable, whitespace
import argparse

ROOT_DIR = Path(__file__).parents[1]
CONTENT_DIR = ROOT_DIR / "content"


def sanitize_fname(s: str):
    valid = ascii_lowercase + digits + whitespace
    s = s.lower()
    s = filter(lambda x: x in valid, s)
    s = "".join(s)
    s = s.split()
    s = "_".join(s)
    return s


if __name__ == "__main__":
    # set logging
    logging.basicConfig(level=logging.INFO)

    # get args
    parser = argparse.ArgumentParser()
    parser.add_argument("category")
    args = parser.parse_args()

    # get title
    title = input(">>> Note title: ")
    logging.info(f"Title: {title}")

    # get timestamp
    date = datetime.datetime.now()
    date = date.strftime("%Y-%m-%d")

    # get filename
    fname = sanitize_fname(title)
    fname = f"{date}_{fname}"
    logging.info(f"Filename: {fname}")

    # create content
    path = f"{args.category}/{fname}/index.md"
    cmd = ["hugo", "new", path]
    logging.info(f"Hugo command: {cmd}")
    subprocess.run(cmd)
