def load(file_name, data):
    with open(file_name, "w") as fp:
        fp.write(data)

    print("Data loaded successfully.")  