from os import listdir, mkdir
from sys import argv,stdout
from toolbox import println, panic

import md
import pdf

def build_all(m) -> None:
    m.setup()

    TEXTS_FOLDER = "./scrīpta/"
    texts_folders = listdir(TEXTS_FOLDER)
    for folder in texts_folders:
        folder_path = TEXTS_FOLDER + f"{folder}/"

        println(stdout, f"Building {m.FORMAT_NAME} document for {folder}")

        for file in listdir(folder_path):
            if file.endswith(".tex"):
                m.build_file(folder_path + f"{file}")

def main(args: list) -> None:
    try:
        mkdir('builds')
    except FileExistsError:
        pass

    if not args:
        build_all(md)
        build_all(pdf)
    elif args[0] == "md":
        build_all(md)
    elif args[0] == "pdf":
        build_all(pdf)
    else:
        panic(f"ERROR: unknown target format: {args[0]}")

if __name__ == '__main__':
    main(argv[1:])