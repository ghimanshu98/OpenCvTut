import cv2 as cv
import numpy as np

# creating a blank canvas / we can also load image to draw on that.
canvas = np.zeros((500,500,3), np.uint8)
cv.imshow('Blank', canvas)

# creating a recatangle on the canvas
cv.rectangle(canvas, (0,0), (250,250), (255,0,134), thickness= 2)
cv.imshow('Rectangle', canvas)

canvas = np.zeros((500,500,3), np.uint8)
# creating a recatangle on the canvas
cv.rectangle(canvas, (0,0), (250,250), (255,0,134), thickness= -1) # or thickness = cv.FILLED
cv.imshow('Filled Rectangle', canvas)

canvas = np.zeros((500,500,3), np.uint8)
# Creating a circle on the canvas
cv.circle(canvas, center=(250,250), radius= 100, color= (255,0,134), thickness= 5)
cv.imshow('Circle', canvas)

canvas = np.zeros((500,500,3), np.uint8)
# Creating a circle on the canvas
cv.circle(canvas, center=(250,250), radius= 100, color= (255,0,134), thickness= -1)
cv.imshow('Circle Filled', canvas)

canvas = np.zeros((500,500,3), np.uint8)
# creating a line
cv.line(canvas, pt1=(0,0), pt2=(250,250), color= (255,0,134), thickness =3)
cv.imshow('Line', canvas)

canvas = np.zeros((500,500,3), np.uint8)
# Writing Text
cv.putText(canvas, text= "Hello World! :)", org= (23, 250), fontFace= cv.FONT_HERSHEY_TRIPLEX, fontScale= 1, color= (255,0,134), thickness= 3)
cv.imshow('Text', canvas)


cv.waitKey(0)