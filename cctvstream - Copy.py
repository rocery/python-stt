import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture()
# cap.open('http://192.168.15.187:4747/video')

cap.open('http://192.168.15.201/')

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# print(height)

# print(width)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    resize_img = cv2.resize(frame, (800, 600))
    cv2.imshow('DVR Test', resize_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()