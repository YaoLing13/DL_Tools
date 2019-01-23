import os
import sys
import argparse

parser = argparse.ArgumentParser(description='Get file absulte ')
parser.add_argument('src_path', help='Path to src path.')
parser.add_argument('save_file', help='Path to save file name.')

if __name__ == '__main__':
    args = parser.parse_args()
    src_path = args.src_path
    save_file = args.save_file
    files = os.listdir(src_path)
    with open(save_file, 'w') as fp:
        names = ''
        for file in files:
            if file[-3:] == "xml":
                name = src_path + '/' + file + '\n'
                names = names + name
        fp.write(names)



