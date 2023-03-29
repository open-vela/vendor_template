import os
import argparse

def replace_in_file(file_path, replacements):
    with open(file_path, 'r') as f:
        content = f.read()
    for old, new in replacements.items():
        content = content.replace(old, new)
    with open(file_path, 'w') as f:
        f.write(content)

def replace_in_dir(dir_path, replacements):
    path = dir_path
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            replace_in_file(file_path, replacements)
        for dir in dirs:
            path = os.path.join(root, dir)
            replace_in_dir(path, replacements)
    for root, dirs, files in os.walk(dir_path):
        for dir_name in dirs:
            for old, new in replacements.items():
                if old in dir_name:
                    new_dir_name = dir_name.replace(old, new)
                    os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))
        for file_name in files:
            for old, new in replacements.items():
                if old in file_name:
                    new_file_name = file_name.replace(old, new)
                    os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Replace patterns in directory')
    parser.add_argument('new_vendor_name', type=str, help='New vendor name')
    parser.add_argument('new_board_name', type=str, help='New board name')
    parser.add_argument('new_chip_name', type=str, help='New chip name')
    args = parser.parse_args()

    replacements = {
        "vendor_name": args.new_vendor_name,
        "board_name": args.new_board_name,
        "chip_name": args.new_chip_name,
        "VENDOR_NAME": args.new_vendor_name.upper(),
        "BOARD_NAME": args.new_board_name.upper(),
        "CHIP_NAME": args.new_chip_name.upper()
    }

    replace_in_dir("boards", replacements)
    replace_in_dir("chips", replacements)
