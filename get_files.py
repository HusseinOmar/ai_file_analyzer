import os

supported_exts = ["c", "cpp", "cs", "css", "doc", "docx", "go", "html", "java",
                  "js", "json", "md", "pdf", "php", "pptx", "py", "rb", "sh", "tex", "ts", "txt"]
# => List from string


def get_list_from_string(string):
    return string.split(",")


def get_exts_from_user():
    print('============================================================')
    print(f'Supported file extensions {supported_exts}')
    exts_str_raw = input(
        "Enter the file extension(s) separated by commas (no spaces): ")
    exts_str = exts_str_raw.replace(" ", "")
    print('============================================================')
    return get_list_from_string(exts_str)


def validate_ext(ext_list):
    final = True
    for ext in ext_list:
        if ext not in supported_exts:
            print(f"xxx ==> Invalid file extension: {ext}")
            final = False
    return final


def get_exts_list():
    x = False
    while not x:
        file_ext_list = get_exts_from_user()
        x = validate_ext(file_ext_list)
    return file_ext_list


def get_path():
    print('============================================================')
    print('')
    path = input(
        " $$ => Enter the path to the file(s) - local folder is default [Enter]: ")
    if path == "":
        path = "./"
    return path


def get_file_names():
    while True:
        path = get_path()
        try:
            all_files = os.listdir(path)
        except FileNotFoundError:
            print(f'xxx ==> Invalid path: {path}')
            continue
        break
    file_names = []
    file_extensions = get_exts_list()
    for file in all_files:
        extension = file.rsplit('.', 1)[-1]
        for ext in file_extensions:
            if extension == ext:
                file_names.append(file)
    if file_names == []:
        print(
            f'xxx ==> No files with the following extensions: {file_extensions}')
    return path, file_names


def get_files():
    x = False
    while not x:
        path, file_names = get_file_names()
        if not file_names:
            continue
        print(f'The following files will be processed: ')
        for file in file_names:
            print(f' ==> {file}')
        accept = input("Do you accept these files? [y/n]: ")
        if accept == "y" or accept == "Y" or accept == "yes" or accept == "Yes":
            x = True
            return path, file_names
