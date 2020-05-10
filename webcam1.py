import cv2

from PIL import ImageFont, ImageDraw, Image
import numpy

#capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture("20200202_233046.mp4")
#cap_i = cv2.VideoCapture("20200422_121908.mp4")

while True:
    ret, frame = capture.read()
    if not ret:
        break
    #cv2.imshow("frame", frame[:,:,:])
    frame1 = frame[:, :, 1]
    print(frame1.shape)
    ret, frame1 = cv2.threshold(frame1,50, 255, cv2.THRESH_BINARY)
    cv2.imshow("frame1", frame1)
    frame1 =  cv2.cvtColor(frame1, cv2.COLOR_GRAY2BGR)
    frame1 = frame1 & frame
    cv2.imshow("frame3", frame1)
    if cv2.waitKey(1) > 0:
        break

capture.release()
cv2.destroyAllWindows()