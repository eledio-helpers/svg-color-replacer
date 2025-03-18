import os
import glob

OLD_COLORS = ["black", "#000000"]
NEW_COLOR = "#141B5D"

FOLDER_PATH = "img"


def main():
    for file_path in glob.glob(os.path.join(FOLDER_PATH, "*.svg")):
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()


        for old_color in OLD_COLORS:
            content = content.replace(old_color, NEW_COLOR)


        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

if __name__ == "__main__":
    main()
