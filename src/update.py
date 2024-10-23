import tempfile
import os
import subprocess
import shutil
import json

from filecmp import cmp
from pathlib import Path

from data.get_data_path import get_project_directory


def download_files():
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            subprocess.run(["git", "clone", "https://github.com/ZakiarV/TTWGMCalculator.git", temp_dir], check=True)
            access_files_to_update = os.path.join(temp_dir, "data", "files_to_update.json")
            with open(access_files_to_update) as f:
                files_to_update = json.load(f)
            print(files_to_update)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def update():
    download_files()
