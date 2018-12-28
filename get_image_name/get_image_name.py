import os
import sys
import argparse

def get_image_name(image_path, save_dir, save_name):
    names = os.listdir(image_path)
    save_file = save_dir + '/' + save_name
    txt_file = open(save_file, 'w')
    for name in names:
        image_name = name[:-4] + '\n'
        txt_file.write(image_name)
    txt_file.close()
    print('Path Done!')


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--image_dir", default="", help="The directory path which file exits")
    args.add_argument("--save_dir", default="./", help="The directory path which save")
    args.add_argument("--save_name", default="image_name.txt", help="The file name which would generate")
    FLAGS = args.parse_args()

    if len(FLAGS.image_dir) == 0:
        print("Please Input 'image_dir' !")
        exit()
    get_image_name(FLAGS.image_dir, FLAGS.save_dir, FLAGS.save_name)