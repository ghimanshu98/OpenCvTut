import cv2 as cv

def rescale_frame(frame, scale = 0.75):
    """ will work for img, video, live_video """
    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)

    # creating a tuple of height & width
    dim = (width, height)

    # calling the cv resize method
    return cv.resize(frame, dim, interpolation= cv.INTER_AREA)

def changeRes(capture, width, height):
    """ works for Live Video """

    capture.set(3, width) # for setting the new width
    capture.set(4, height) # for setting the new height

