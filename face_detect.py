# -*- coding: utf-8 -*-
from __future__ import print_function
import click
import os
import re
import face_recognition.api as face_recognition
import multiprocessing
import sys
import itertools
import cv2

def test_image(image_to_check):
    unknown_image = face_recognition.load_image_file(image_to_check)
    face_locations = face_recognition.face_locations(unknown_image, number_of_times_to_upsample=0, model='CNN')

    cap_i = cv2.VideoCapture(image_to_check)
    ret, frame = cap_i.read()
    n = 0
    for face_location in face_locations:
        top, right, bottom, left = face_location
        h = int((bottom - top) / 2)
        w = int((right - left)/ 3)
        fname_sub = frame[max(0, top-h):bottom+h, max(0, left-w):right+w]
        fname = 'gen_' + image_to_check.replace('.jpg', '') + '_'+  str(n) +'.jpg'
        cv2.imwrite(fname, fname_sub)
        n += 1
    print(f"file={image_to_check}, face={n}")

def image_files_in_folder(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if re.match(r'.*\.(jpg|jpeg|png)', f, flags=re.I)]
@click.command()
@click.argument('image_to_check')
def main(image_to_check):
    if os.path.isdir(image_to_check):
        [test_image(image_file) for image_file in image_files_in_folder(image_to_check)]
    else:
        test_image(image_to_check)
if __name__ == "__main__":
    main()
