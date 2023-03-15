import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# obtaining an image
img = cv.resize(src= cv.imread('images/c.jpg'), dsize= (900,600), interpolation= cv.INTER_AREA)
cv.imshow("ORIGINAL IMAGE", img)

# converting to gray scale
gray = cv.cvtColor(img, code= cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)


# Creating a mask, and pass it as an arg in calHist method
canvas = np.zeros(shape= gray.shape[:2], dtype='uint8')
circle = cv.circle(canvas, center = (gray.shape[1]//2, gray.shape[0]//2), radius= 200, thickness= -1, color= 255)
cv.imshow('circle', circle)

# creating masked image using bitwise operation
masked = cv.bitwise_and(gray, gray, mask = circle)
cv.imshow('mask', masked)

# creating histogram
gray_hist = cv.calcHist(images= [gray], channels= [0], mask = masked, histSize= [256], ranges=[0,256])

# plotting the hist using matplotlib
plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0,256]) 
plt.show()


# plotting histogram for color images
color = ('b','g','r')
plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
for i, col in enumerate(color):
    print(i, col)
    hist = cv.calcHist(images=[img], channels= [i], mask = None, histSize=[256], ranges=[0,256])
    plt.plot(hist, color = col)
    plt.xlim([0,256])
plt.show()

cv.waitKey(0)