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
            if not os.path.exists(access_files_to_update):
                raise FileNotFoundError("files_to_update.json not found")
            with open(access_files_to_update, "r") as f:
                files_to_update = json.load(f)
            for file in files_to_update["files_to_update"]:
                file_path = os.path.join(get_project_directory(), file)
                if not os.path.exists(file_path):
                    raise FileNotFoundError(f"{file} not found")
                if not cmp(file_path, os.path.join(temp_dir, file)):
                    shutil.copyfile(os.path.join(temp_dir, file), file_path)
                    print(f"{file} updated")
                else:
                    print(f"{file} is up to date")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def update():
    download_files()
