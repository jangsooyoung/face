import cv2

from PIL import ImageFont, ImageDraw, Image

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = capture.read()
    #np_frame = Image.fromarray(frame)
    #s_np_frame = cv2.resize(np_frame, (150, 200))
    #frame = Image.fromarray(s_np_frame)
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) > 0:
        break

capture.release()
cv2.destroyAllWindows()
