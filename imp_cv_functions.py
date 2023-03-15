import cv2 as cv

# importing an image
img = cv.imread('images/c.jpg')
# cv.imshow('Original', img)

# resizing the image
img = cv.resize(img, dsize=(500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized', img)

# converting to grayscale
cv.imshow('GrayScale', cv.cvtColor(img, code= cv.COLOR_BGR2GRAY))

# blurring an image
blurred = cv.GaussianBlur(img, ksize=(3,3), sigmaX= cv.BORDER_DEFAULT)
cv.imshow('Blurred', blurred)

# finding edge of image
canny = cv.Canny(image= blurred, threshold1= 125, threshold2= 175)
cv.imshow('Blurred-Edged', canny)

# Dilating the edged image
dilated = cv.dilate(canny, kernel= (3,3), iterations= 1)
cv.imshow('Dilated-Edged', dilated)

# Eroding (Used to reverse dilation to some extent)
eroded = cv.erode(dilated, kernel= (3,3), iterations= 1)
cv.imshow('Eroded-dilated', eroded)

# cropping an image - uses array slicing
cropped = img[150:300, 300:450]
cv.imshow('Cropped', cropped)


cv.waitKey(0)