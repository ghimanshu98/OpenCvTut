import cv2 as cv
import numpy as np

# ontaining the image
img = cv.resize(src= cv.imread('images/g.jpg'), dsize= (900,600), interpolation= cv.INTER_AREA)
cv.imshow("ORIGINAL IMAGE", img)

# Creating a blank image to draw a circle on it
canvas = np.zeros(shape= img.shape[:2], dtype= 'uint8')
cv.imshow('Canvas', canvas)

# creating the mask
mask = cv.circle(canvas, center= (img.shape[1]//2, img.shape[0]//2), radius= 200, color= 255, thickness= -1)
cv.imshow('mask', mask)

# Applying mask on the image using bitwise and operation
masked_img = cv.bitwise_and(img,img, mask = mask)
cv.imshow('masked image', masked_img)

cv.waitKey(0)