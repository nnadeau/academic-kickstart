import logging
import subprocess
from pathlib import Path
from typing import Optional

import fire
import nbconvert
import nbformat


def main(path: Optional[str] = None):
    if path:
        paths = [Path(path)]
    else:
        # glob notebooks
        paths = list((Path.cwd() / "content").rglob("*.ipynb"))
        paths = [p for p in paths if ".ipynb_checkpoints" not in str(p.resolve())]
        logging.info(f"Globbed {len(paths)} notebooks")

    logging.info(f"Paths to convert: {paths}")

    # convert
    for p in paths:
        logging.info(f"Exporting {p}")

        args = ["jupyter", "nbconvert", p, "--to", "markdown"]
        subprocess.run(args)

        output = p.with_suffix(".md")
        try:
            with open(output) as f:
                text = f.read()
        except FileNotFoundError as e:
            logging.error(e)
            exit(1)

        text = text.replace('<table border="1"', "<table")
        with open(output, "w") as f:
            f.write(text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fire.Fire(main)
