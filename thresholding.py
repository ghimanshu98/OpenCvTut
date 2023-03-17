import numpy as np
import cv2 as cv

# loading an image
img = cv.resize(cv.imread('images/c.jpg'), dsize= (900,600), interpolation= cv.INTER_AREA)
cv.imshow('ORIGINAL', img)

# BGR to GRAY
gray = cv.cvtColor(img, code= cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale', gray)

# Simple thresholding
threshold, thresh = cv.threshold(gray, thresh=150, maxval=255, type= cv.THRESH_BINARY)
print(f'Simple Threshold values {threshold}')
cv.imshow('SImple threshold', thresh)

## simple inverse thresholding - > values less then thresh -> 255 and values greater then thresh -> 0
threshold, thresh_inv = cv.threshold(gray, thresh=150, maxval=255, type= cv.THRESH_BINARY_INV)
print(f'Simple Threshold values inv {threshold}')
cv.imshow('SImple threshold inv', thresh_inv)

# Adaptive thresholding
adaptive_thresold = cv.adaptiveThreshold(gray, maxValue= 255, adaptiveMethod= cv.ADAPTIVE_THRESH_MEAN_C, thresholdType= cv.THRESH_BINARY, blockSize= 11, C=0)
cv.imshow('Adaptive Thresholding', adaptive_thresold)

## adaptive inverse thresholding
adaptive_thresold_inv = cv.adaptiveThreshold(gray, maxValue= 255, adaptiveMethod= cv.ADAPTIVE_THRESH_MEAN_C, thresholdType= cv.THRESH_BINARY_INV, blockSize= 11, C=0)
cv.imshow('Adaptive Thresholding I=inv' , adaptive_thresold_inv)

cv.waitKey(0)