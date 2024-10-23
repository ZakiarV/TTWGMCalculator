import tempfile
import os
import subprocess
import shutil
import json

from filecmp import cmp
from pathlib import Path

from data.get_data_path import get_data_path


def files_to_update():
    files_to_update_path = os.path.join(get_data_path(), "files_to_update.json")
    with open(files_to_update_path, "r") as f:
        files = json.load(f)

    return files


def download_files():
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            subprocess.run(["git", "clone", "", temp_dir], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def update():
    download_files()