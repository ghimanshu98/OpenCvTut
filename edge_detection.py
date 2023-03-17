import cv2 as cv
import numpy as np

# load image
img = cv.resize(cv.imread('images/c.jpg'), dsize=(900,600), interpolation= cv.INTER_AREA)
cv.imshow('ORIGINAL', img)

# convert to grayscale
gray = cv.cvtColor(img, code = cv.COLOR_BGR2GRAY)
cv.imshow('GRAYSCALE', gray)

# Edge Detection 

#1) using canny - most used
cv.imshow('CannyEdge', cv.Canny(gray, threshold1=150, threshold2=255))

#2) using Laplacian - least used
lap = cv.Laplacian(gray, ddepth= cv.CV_64F)

# converting to absolute
lap = np.uint8(np.abs(lap))

cv.imshow('Laplacian edge', lap)

#3) using Sobel - used in most advanced cases, canny aslo internally uses sobel
sobel_x = cv.Sobel(gray, ddepth=cv.CV_64F, dx = 1, dy= 0)
cv.imshow('Sobel_x', sobel_x)
sobel_y = cv.Sobel(gray, ddepth=cv.CV_64F, dx = 0, dy= 1)
cv.imshow('Sobel_y', sobel_y)

sobel_combined = cv.bitwise_or(sobel_x, sobel_y)
cv.imshow('Sobel_combined',sobel_combined)
cv.waitKey(0)