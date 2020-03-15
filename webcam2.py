import cv2

from PIL import ImageFont, ImageDraw, Image
import numpy

#cap_i = cv2.Videocap_i(0)
cap_i = cv2.VideoCapture("test.mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
cap_o = cv2.VideoWriter('out.mp4', fourcc, 30.0, (1280,720))
while True:
    ret, frame = cap_i.read()
    if not ret:
        break
    cv2.imshow("frame", frame)

    frame1 = frame[:, :, 2]
    cv2.imshow("frame1", frame1)

    ret, frame2 = cv2.threshold(frame1, 130, 255, cv2.THRESH_BINARY)
    frame3 = cv2.cvtColor(frame2, cv2.COLOR_GRAY2BGR)
    cv2.imshow("frame3", frame3)

    frame4 = frame3 & frame
    cap_o.write(frame4)
    cv2.imshow("frame4", frame4)

    if cv2.waitKey(30) > 0:
        break

cap_o1.release()
cap_o2.release()
cap_o3.release()
cap_o4.release()
cap_i.release()
cv2.destroyAllWindows()
