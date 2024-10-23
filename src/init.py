import json

from data.get_data_path import get_data_path


def load_data_from_json():
    data_path = get_data_path()
    data = {"settings": {},
            "resources": {},
            "buildings": {},
            "units": {}
            }

    with open(data_path + "/config/settings.json") as f:
        data["settings"] = json.load(f)

    with open(data_path + "/config/resources.json") as f:
        data["resources"] = json.load(f)

    with open(data_path + "/config/buildings.json") as f:
        data["buildings"] = json.load(f)

    with open(data_path + "/config/units.json") as f:
        data["units"] = json.load(f)

    return data


def load_data_from_save_file(game_name):
    data_path = get_data_path()
    data = {"resources": {},
            "buildings": {},
            "units": {}
            }
    try:
        with open(data_path + f"/saves/{game_name}.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        pass

    return data


def save_data_to_save_file(data, game_name):
    data_path = get_data_path()
    with open(data_path + f"/saves/{game_name}.json", "w") as f:
        json.dump(data, f, indent=4)
    return
