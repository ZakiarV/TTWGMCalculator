import os


def get_data_path():
    return os.path.join(os.path.dirname(__file__))


def get_project_directory():
    return os.path.dirname(os.path.dirname(__file__))

print(get_project_directory())