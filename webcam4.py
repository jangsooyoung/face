import cv2

from PIL import ImageFont, ImageDraw, Image
import numpy
import imutils
import os

def filter(contours):
    r_contours = []
    x=y=w=h=max_sz=0
    for contour in contours:
        area = cv2.contourArea(contour)
        (x1, y1, w1, h1) = cv2.boundingRect(contour)
        if w1*h1 > max_sz:
            max_sz = w1 * h1
            (x, y, w, h) = (x1, y1, w1, h1)
            r_contours.append(contour)
    return (x, y, w, h), r_contours

def conv(fname):
    i = 0
    print(fname)
    cap_i = cv2.VideoCapture('mp4s/'+fname +".mp4")
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    cap_o = cv2.VideoWriter('mp4o/'+fname +'_o4.mp4', fourcc, 25.0, (960,540))
    while True:
        ret, frame = cap_i.read()
        if not ret:
            break
        frame0 = frame #cv2.resize(frame, (960, 540))
        #cv2.imshow("frame0", frame0)
        frame1 = frame0[:, :, 2]

        ret, frame2 = cv2.threshold(frame1, 120, 255, cv2.THRESH_BINARY)
        frame3 = cv2.cvtColor(frame2, cv2.COLOR_GRAY2BGR)
        image, contours, hierarchy = cv2.findContours(frame2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        frame4 = frame3 & frame0
        frame5 = None
        try:
            r, r_contours = filter(contours)
            if r[3] <= 0 or r[2] <= 0:
                continue
            # if r_contours is not None:
            #    cv2.drawContours(frame4, r_contours, -1, (0, 256, 0), 0)
            #cv2.rectangle(frame4, (r[0], r[1]), (r[0] + r[2], r[1] + r[3]), (256, 0, 0), 2)
            frame5 = frame4[r[1]:r[1] + r[3], r[0]:r[0] + r[2]]
            cap_o.write(frame5)
            #cv2.imshow("frame5", frame5)
            cv2.imwrite('jpg/'+fname + f"_{i}.jpg", frame5)
            i+=1
        except Exception as err:
            print(f"error {err}")
        if cv2.waitKey(30) > 0:
           break
    cap_o.release()
    cap_i.release()
    print(f'close {fname}')

filenames = os.listdir("mp4s")
for filename in filenames:
    if filename.startswith("k") and filename.index('.mp4'):
        conv(filename.replace('.mp4', ''))

cv2.destroyAllWindows()
