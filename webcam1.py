import cv2

from PIL import ImageFont, ImageDraw, Image
import numpy

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("test.mp4")

while True:
    ret, frame = capture.read()
    if not ret:
        break
    #cv2.imshow("frame", frame[:,:,:])
    frame1 = frame[:, :, 2]
    ret, frame1 = cv2.threshold(frame1, 130, 255, cv2.THRESH_BINARY)
    frame1 =  cv2.cvtColor(frame1, cv2.COLOR_GRAY2BGR)
    frame1 = frame1 & frame
    cv2.imshow("frame1", frame1)
    if cv2.waitKey(1) > 0:
        break

capture.release()
cv2.destroyAllWindows()