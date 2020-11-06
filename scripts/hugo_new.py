import logging
import subprocess
from datetime import datetime
from pathlib import Path
from string import ascii_lowercase, digits, whitespace

import fire
import nbformat as nbf


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


def new(kind: str, notebook: bool = False):
    # get title
    title = get_title()
    title = sanitize_fname(title)

    # get datetime
    now = datetime.now()

    # set path
    path = f"{kind}/{now.year}/{now.month}/{title}"

    # create
    cmd = ["hugo", "new", path]
    logging.info(f"Hugo command: {' '.join(cmd)}")
    subprocess.run(cmd)

    if notebook:
        path = Path.cwd() / "content" / path
        _create_notebook(path.resolve())


def _create_notebook(dir_path: Path):
    # get metadate to copy to notebook
    index_path = dir_path / "index.md"
    with open(index_path) as f:
        meta = f.read().splitlines()

    # strip comments (they look bad in jupyter)
    meta = [m for m in meta if not m.startswith("#")]

    # add newline to end to prevent ugly jupyter renders
    meta.append("\n")

    # join meta into text
    meta = "\n".join(meta)

    # create notebook
    nb = nbf.v4.new_notebook()
    nb["cells"] = [nbf.v4.new_markdown_cell(meta)]
    nbf.write(nb, index_path.with_suffix(".ipynb"))


if __name__ == "__main__":
    # set logging
    logging.basicConfig(level=logging.INFO)

    # run cli
    fire.Fire()
