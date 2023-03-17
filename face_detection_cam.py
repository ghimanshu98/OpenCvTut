import cv2 as cv
from rescale import *

# open video capture
cam_feed = cv.VideoCapture(0)

# loading th harcascade face classifier
har_clf = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# while cam is open
while True:
    isTrue, frame = cam_feed.read()
    # rescaling the feed
    # frame = rescale_frame(frame)

    # graying the frame
    gray = cv.cvtColor(frame, code = cv.COLOR_BGR2GRAY)
    
    # applying face detector
    face_cordinates = har_clf.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 3)

    # drawing face cordinates on cam feed
    for (x,y,w,h) in face_cordinates:
        cv.rectangle(frame, pt1= (x,y), pt2=(x+w, y+h), color=(0,159,255), thickness= 2)
    cv.imshow(f'Webcam feed, Face Detected {len(face_cordinates)}', frame)

    # to stop cam feed
    if cv.waitKey(0) & 0xFF == ord('d'):
        break

# releasing cam
cam_feed.release()
cv.destroyAllWindows()
    

