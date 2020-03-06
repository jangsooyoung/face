import face_recognition
import cv2
import camera
import os
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import sys, getopt
import IPython.display 
get_ipython().system('tree')
IPython.display.Image(filename='/j/cop/knowns/성민.jpg', width=150,height=200)
np_img1 = face_recognition.load_image_file('/j/cop/knowns/성민.jpg')
np_img1 = cv2.resize(np_img1, (300, 400))
h = np_img1.shape[0]
w = np_img1.shape[1]
print(h, w)
print(np_img1.shape)
lmark = face_recognition.face_landmarks(np_img1)
print(type(lmark), len(lmark[0]), lmark[0])
for m in lmark[0]:
    print(m)
for mlist in lmark[0]:
    for p in lmark[0][mlist]:
        p2 = tuple([p1 + 1 for p1 in p]) # (x, y), (x+1,y+1)
        cv2.rectangle(np_img1, p, p2, (255, 255, 0), -1)
display(Image.fromarray(np_img1))
dirname = '/j/cop/knowns'
files = os.listdir(dirname)
known_face_encodings = []
known_face_names = []
for filename in files:
    name, ext = os.path.splitext(filename)
    known_face_names.append(name)
    pathname = os.path.join(dirname, filename)
    img = face_recognition.load_image_file(pathname)
    print(f"사전 파악 인물[{pathname}] ", end='')
    face_encodings = face_recognition.face_encodings(img, num_jitters=10)
    if len(face_encodings) > 0:
        face_encoding = face_recognition.face_encodings(img)[0]
        print("{face_encodings}")
        known_face_encodings.append(face_encoding)
face_locations = []
face_encodings = []
face_names = []
target_file = '/j/cop/20191120_114007.jpg'
np_frame = cv2.imread(target_file)
np_frame= np_frame[:, :, ::-1]
print("find[{}/{}]".format(type(np_frame).__name__, np_frame.shape))
np_resize_frame = cv2.resize(np_frame, (150, 200))

display(Image.fromarray(np_frame))
np_rgb_frame = np_frame # np_frame[:, :, ::-1]
face_locations = face_recognition.face_locations(np_rgb_frame)
face_encodings = face_recognition.face_encodings(np_rgb_frame, face_locations)
face_names = []
print(face_locations)
for face_encoding in face_encodings:
    # 기등록 인물과 유사도 
    distances = face_recognition.face_distance(known_face_encodings, face_encoding)
    #print(face_encoding)
    min_value = min(distances)
    # tolerance: How much distance between faces to consider it a match. Lower is more strict.
    # 0.6 is typical best performance.
    name = "Unknown"
    #print(f">>>>>>>>>>>>>>>>>>>>>>>>{min_value}:{face_encoding}")
    #print(min_value)
    if min_value < .35  : #0.35: # 0.6
        index = np.argmin(distances)
        name = known_face_names[index]
    face_names.append(name)
print(face_names)
font = ImageFont.truetype("/j/cop/gulim.ttc", 20)
for (top, right, bottom, left), name in zip(face_locations, face_names):
    print (top, right, bottom, left)
    box_rgb = (55, 144, 130)#(0, 255, 0)#
    # Draw a box around the face
    if name == "Unknown":
        cv2.rectangle(np_frame, (left, top), (right, bottom), box_rgb, -1)#cv2.FILLED)
    else:
        cv2.rectangle(np_frame, (left, top), (right, bottom), box_rgb, 4)
    # Draw a label with a name below the face
    cv2.rectangle(np_frame, (left, bottom - 35), (right, bottom), box_rgb, cv2.FILLED)
    
    img_pil = Image.fromarray(np_frame)
    #img_pil = cv2.cvtColor(img_pil, cv2.COLOR_BGR2RGB)
    draw = ImageDraw.Draw(img_pil)
    draw.text((left+10, bottom - 25), name, font=font, fill=(255, 255, 255, 0))
    np_frame =  np.array(img_pil)
np_resize_frame = cv2.resize(np_frame, (150, 200))
display(Image.fromarray(np_frame))
