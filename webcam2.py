import cv2

from PIL import ImageFont, ImageDraw, Image
import numpy
import imutils

def filter(contours):
    r_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        x, y, w, h = cv2.boundingRect(contour)
        if 1000 < area:
            r_contours.append(contour)
    return (x,y,w,h), r_contours

#  입력 Image
#cap_i = cv2.Videocap_i(0)
cap_i = cv2.VideoCapture("20200202_233046.mp4")

#출력 image
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
cap_o = cv2.VideoWriter('out.mp4', fourcc, 30.0, (1280,720))
#background image
backg = cv2.imread(' backg4.jpg')
backg = cv2.resize(backg, (1280,720), interpolation=cv2.INTER_AREA)

while True:
    ret, frame = cap_i.read()
    if not ret:
        break
    frame1 = frame[:, :, 2]
    ret, frame2 = cv2.threshold(frame1, 130, 255, cv2.THRESH_BINARY)
    frame3 = cv2.cvtColor(frame2, cv2.COLOR_GRAY2BGR)
    cv2.imshow("frame2", frame2)
    image, contours, hierarchy = cv2.findContours(frame2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    r, r_contours = filter(contours)

    print(frame3)
    # 손만 부분만 남기기
    #frame4 = (frame & frame3) & (backg & [(c == 0 and 1 or 0) for c in frame3])
    #if contours is not None:
    #    cv2.drawContours(frame4, r_contours, -1, (0, 256, 0), 2)
    #cv2.rectangle(frame4, (r[0], r[1]), (r[0] + r[2], r[1] + r[3]), (256, 0, 0), 2)

    cap_o.write(frame4)
    cv2.imshow("frame4", frame4)
    if cv2.waitKey(30) > 0:
        break
cap_o.release()
cap_i.release()
cv2.destroyAllWindows()
