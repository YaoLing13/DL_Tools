'''

Description : Generate video from images


Author: Yao Ling
Time  : 2018/12/09

'''

import os
import sys
import cv2
import argparse


def main():

    data_detection_txt = FLAGS.image_dir_txt
    save_path = FLAGS.save_dir
    # save_name = save_path + '/' + FLAGS.save_name
    fps = 15

    # write output video
    w = 1280
    h = 960
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    out = cv2.VideoWriter('test_bit.avi', fourcc, fps, (w, h))

    with open(data_detection_txt, 'r') as f:
        for line in f.readlines():
            src_img_path = line.rstrip()
            frame = cv2.imread(src_img_path)
            if frame is None:
                print('Canot open image:', src_img_path)
                continue

            # write output video
            cv2.imshow('img', frame)
            out.write(frame)
            cv2.waitKey(1)
    print("Done!")



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir_txt', type=str, default='', help='Directory where to get image filepath!')
    parser.add_argument('--save_dir', type=str, default='', help='Directory where to save image!!!')
    parser.add_argument('--save_name', type=str, default='', help='Directory where to save image!!!')
    FLAGS, unparsed = parser.parse_known_args()
    main()
