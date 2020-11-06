import logging
from pathlib import Path
from typing import Optional

import fire
import requests

ROOT_DIR = Path(__file__).parents[1]
CONTENT_DIR = ROOT_DIR / "content"
BASE_URL = "https://unsplash.com/photos"


def get_latest_post_dir():
    md_paths = list(CONTENT_DIR.rglob("index.md"))
    md_paths = sorted(md_paths, key=lambda x: x.stat().st_ctime, reverse=True)
    latest_dir = md_paths[0].parent
    logging.info(f"Latest dir: {latest_dir}")
    return latest_dir


def create_image(image_id: Optional[str] = None, dir_path: Optional[str] = None):
    # get image ID
    if not image_id:
        image_id = input("Image ID: ")
    image_id = image_id.strip()

    # set output dir and path
    if dir_path:
        dir_path = Path(dir_path)
    else:
        dir_path = get_latest_post_dir()
    output_path = dir_path / "featured.jpg"

    # fetch image
    url = f"{BASE_URL}/{image_id}/download"
    r = requests.get(url)
    logging.info(f"Request: {r}")
    with open(output_path, "wb") as f:
        f.write(r.content)


if __name__ == "__main__":
    # set logging
    logging.basicConfig(level=logging.INFO)

    # run clio
    fire.Fire()
