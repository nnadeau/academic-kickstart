import logging
import subprocess
from string import ascii_lowercase, digits, whitespace

import fire


def sanitize_fname(s: str):
    valid = ascii_lowercase + digits + whitespace
    s = s.lower()
    s = filter(lambda x: x in valid, s)
    s = "".join(s)
    s = s.split()
    s = "-".join(s)
    return s


def get_title():
    title = input(">>> Note title: ")
    logging.info(f"Title: {title}")
    return title


def new(kind: str):
    # get title
    title = get_title()
    title = sanitize_fname(title)

    path = f"{kind}/{title}"
    cmd = ["hugo", "new", path]
    logging.info(f"Hugo command: {' '.join(cmd)}")
    subprocess.run(cmd)


if __name__ == "__main__":
    # set logging
    logging.basicConfig(level=logging.INFO)

    # run clio
    fire.Fire()
