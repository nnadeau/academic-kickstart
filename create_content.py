#!/usr/bin/env python3

import argparse
from datetime import datetime
import logging
import subprocess

logging.basicConfig(level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("name", type=str, nargs=1)
parser.add_argument("kind", type=str, nargs="?", default="post")
args = parser.parse_args()

logging.info(f"Args: {args}")

timestamp = datetime.now().date()
logging.info(f"Timestamp: {timestamp}")

name = args.name[0]
name = name.lower()
name = name.split()
name.insert(0, str(timestamp))
name = "-".join(name)

fname = args.kind + "/" + name +".md"
logging.info(f"Fname: {fname}")

subprocess.run(["hugo", "new", fname])
