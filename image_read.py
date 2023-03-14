# importing open cv
import cv2 as cv
from rescale import *

# reading an image in a variable
img = cv.imread("images/a.jpg")

# resizing the image
img2 = rescale_frame(img)

# displaying the image
cv.imshow("Orignal Wallpaper", img)
cv.imshow("Rescaled Wallpaper", img2)
cv.waitKey(0)