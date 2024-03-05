import cv2

cap = cv2.VideoCapture()
# cap.open('http://192.168.15.187:4747/video')

#cap.open('rtsp://admin:admin123@192.168.10.245:554/Streaming/channels/301')
cap.open('rtsp://admin:Admin321@192.168.15.180:554/Streaming/channels/101')

# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

# print(height)

# print(width)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('DVR Test', cv2.WINDOW_NORMAL)

    # Display the resulting frame
    #cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow('DVR Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()