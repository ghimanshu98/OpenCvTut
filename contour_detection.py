import cv2 as cv
import numpy as np

# reading an image
img = cv.resize(cv.imread('images/c.jpg'), dsize= (900,600), interpolation= cv.INTER_AREA)
cv.imshow('Original',img)

# creating a blank canvas
canvas = np.zeros(shape = img.shape, dtype= np.uint8)

# grayscaling the image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GrayScale', gray)

# Contour detection 
# 1) using canny edge detection

canny = cv.Canny(gray,threshold1=125, threshold2= 255)
cv.imshow('Canny Edged', canny)
 
# finding contours
cann_contour, cann_hierarchay = cv.findContours(canny, mode = cv.RETR_LIST, method= cv.CHAIN_APPROX_SIMPLE)

# drawing contuors on blank canvas
con = cv.drawContours(canvas, cann_contour, contourIdx= -1, color= (0,0,255), thickness= 1)
cv.imshow('cann_contours', con)

print(f'{len(cann_contour)} contours found!')

# 2) using threshold edge detection

reter, thres = cv.threshold(src= gray,thresh = 125, maxval = 255, type= cv.THRESH_BINARY)
cv.imshow("threshold Binary", thres)


cv.waitKey(0)