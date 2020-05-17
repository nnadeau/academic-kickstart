from typing import Optional
import logging
import subprocess
from pathlib import Path
import fire

ROOT_DIR = Path(__file__).parents[1]
CONTENT_DIR = ROOT_DIR / "content"


def get_latest_post_dir():
    md_paths = list(CONTENT_DIR.rglob("index.md"))
    md_paths = sorted(md_paths, key=lambda x: x.stat().st_ctime, reverse=True)
    latest = md_paths[0].parent
    logging.info(f"Latest dir: {latest}")
    return latest


def create_image(query: str, dir_path: Optional[str] = None):
    if dir_path:
        dir_path = Path(dir_path)
    else:
        dir_path = get_latest_post_dir()

    path = dir_path / "featured.jpg"
    cmd = ["splash", "--save", str(path.resolve()), "--quiet", "--query", query]
    logging.info(f"Splash command: {' '.join(cmd)}")
    subprocess.run(cmd)


if __name__ == "__main__":
    # set logging
    logging.basicConfig(level=logging.INFO)

    # run clio
    fire.Fire()
