from src.init import load_data_from_json, save_data_to_save_file, load_data_from_save_file


def main():
    data1 = load_data_from_json()
    save_data_to_save_file(data1, "test")
    data2 = load_data_from_save_file("test")
    print(data1 == data2)


if __name__ == "__main__":
    main()
