import numpy as np
import cv2 as cv

# import an image
img = cv.resize(cv.imread('images/c.jpg'), dsize= (900,600), interpolation= cv.INTER_AREA)
cv.imshow('ORIGINAL', img)

# creating a blank canvas
canvas = np.zeros(shape= img.shape[:2], dtype= np.uint8)
cv.imshow('Canvas', canvas)

# splitting the channels B, G, R
b, g, r = cv.split(img)

# displaying the channels - will come in grayscale - show intensity of pixel
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

# merging all channels
merged = cv.merge([b,g,r])
cv.imshow('BGR merged', merged)

# displaying the channel colors in original color using merge method used to merge channels
blue = cv.merge([b, canvas, canvas])
green = cv.merge([canvas, g, canvas])
red = cv.merge([canvas, canvas, r])

cv.imshow('blue_c', blue)
cv.imshow('green_c', green)
cv.imshow('red_c', red)

cv.waitKey(0)

