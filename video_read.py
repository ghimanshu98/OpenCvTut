import cv2 as cv
from rescale import *

# creating video_capyture instance
capture = cv.VideoCapture(0)  # -> 0 for webcam or 1/2/3 for other camera devices or pass the video location to read from file

# creating a for loop to read video frame by frame
while True:
    isTrue, frame = capture.read()  # used to read the frame
    # rescaling the frame
    frame2 = rescale_frame(frame)
    
    # display the frame
    cv.imshow("WebCam Feed", frame)
    cv.imshow("Rescaled Feed", frame2)

    # creating a breaking point
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# releasing the capture 
capture.release()
cv.destroyAllWindows()