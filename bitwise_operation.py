import numpy as np
import cv2 as cv

# creating a canvas
canvas = np.zeros(shape = (400,400), dtype= 'uint8')

# creating 2 images
rectangle = cv.rectangle(canvas.copy(), pt1=(30,30), pt2=(370,370), color= 250, thickness= -1)
circle = cv.circle(canvas.copy(), center=(200,200), radius=200, color=250, thickness= -1)

cv.imshow('Recatangle',rectangle)
cv.imshow('Circle', circle)

# Bitwise AND
bitwise_and = cv.bitwise_and(src1= rectangle, src2= circle)
cv.imshow('Bitwise AND', bitwise_and)

# BItwise OR
bitwise_or = cv.bitwise_or(src1= rectangle, src2= circle)
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(src1= rectangle, src2= circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# Bitwsie NOT - Unary
bitwise_not = cv.bitwise_not(src= rectangle)
cv.imshow('Bitwise NOT rectangle', bitwise_not)

cv.waitKey(0)