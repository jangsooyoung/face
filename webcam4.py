import cv2

from PIL import ImageFont, ImageDraw, Image
import numpy
import imutils

def filter(contours):
    r_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        if 10000 < area:
            r_contours.append(contour)
    return (x,y,w,h), r_contours

#fname = "20200202_233046"
#fname = "20200422_121134"
#fname = "20200422_121403"
#fname = "20200422_121704"
#fname = "20200422_121939"
fname = "20200422_121908"
fname = "20200428_211347"
#

#cap_i = cv2.Videocap_i(0)
cap_i = cv2.VideoCapture(fname +".mp4")

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
cap_o = cv2.VideoWriter(fname +'_o.mp4', fourcc, 30.0, (1280,720))
while True:
    ret, frame = cap_i.read()
    if not ret:
        break
    cv2.imshow("frame", frame)

    frame1 = frame[:, :, 2]
    cv2.imshow("frame1", frame1)

    ret, frame2 = cv2.threshold(frame1, 100, 255, cv2.THRESH_BINARY)
    frame3 = cv2.cvtColor(frame2, cv2.COLOR_GRAY2BGR)
    image, contours, hierarchy = cv2.findContours(frame2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("frame2", frame2)
    r, r_contours = filter(contours)
    frame4 = frame3 & frame
    if contours is not None:
        cv2.drawContours(frame4, r_contours, -1, (0, 256, 0), 0)
    cv2.rectangle(frame4, (r[0], r[1]), (r[0] + r[2], r[1] + r[3]), (256, 0, 0), 2)
    cap_o.write(frame4)
    cv2.imshow("frame4", frame4)
    if cv2.waitKey(30) > 0:
       break

cap_o.release()
cap_i.release()
cv2.destroyAllWindows()