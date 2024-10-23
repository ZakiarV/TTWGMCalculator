from src.init import load_data_from_json, save_data_to_save_file, load_data_from_save_file
from src.update import update


def main():
    data1 = load_data_from_json()
    save_data_to_save_file(data1, "test")
    data2 = load_data_from_save_file("test")
    print(data1 == data2)
    update()



if __name__ == "__main__":
    main()
