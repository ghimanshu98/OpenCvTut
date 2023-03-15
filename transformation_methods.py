import cv2 as cv
import numpy as np

# 1) Translate - shifts image by given pixels in any direction

def translate(image, x, y):
    # translate Matrix
    transMat = np.float32([[1,0,x], [0,1,y]])
    new_dimensions = (image.shape[1], image.shape[0]) # 1->width, 0->height

    # calling warpAffine method to actually set the transalte transformation on the image
    return cv.warpAffine(src= image, M= transMat, dsize= new_dimensions)

# running the above method

# reading and resizing image
img = cv.resize(src = cv.imread('images/c.jpg'), dsize= (500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('Original Image', img)
translated = translate(image= img, x= 100, y= 100)
cv.imshow('Translated Image', translated)


# 2) Rotation - rotate the given image by an angle on a certain point

def rotate(image, angle, rotPoint = None):
    (height, width) = image.shape[:2]
    if rotPoint is None:
        # rotate around center
        rotPoint = (width//2, height//2)
    
    # creating the rotation matrix
    rotMat = cv.getRotationMatrix2D(center= rotPoint, angle= angle, scale= 1.0)

    new_dimensions = (width, height)
    # fixing the rotation matrix obtained on the image
    return cv.warpAffine(src= image, M= rotMat, dsize= new_dimensions)

# running the above method

rotated = rotate(image= translated, angle= 45)
cv.imshow('Rotated', rotated)

# 3) Flipping an image
cv.imshow('Flipped Vertically', cv.flip(img, 0))
cv.imshow('Flipped Horizontally', cv.flip(img, 1))
cv.imshow('Flipped Vertically and Horizontally', cv.flip(img, -1))

cv.waitKey(0)