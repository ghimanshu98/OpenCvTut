import cv2 as cv

# img
img = cv.resize(cv.imread('images/c.jpg'), dsize= (900, 600), interpolation= cv.INTER_AREA)
cv.imshow('ORIGINAL', img)

# Averaging Blur
cv.imshow('Avergare Blur', cv.blur(img, ksize= (5,5)))

# Gaussian Blur
cv.imshow('Gaussian Blur', cv.GaussianBlur(img, ksize= (5,5), sigmaX= 0))

# Median Blur
cv.imshow('Median Blur', cv.medianBlur(img, ksize= 5))

# Bilateral Blur
cv.imshow('Bilateral Blur', cv.bilateralFilter(img, d = 5, sigmaColor= 15, sigmaSpace= 15))

cv.waitKey(0)