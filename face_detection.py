import cv2 as cv

# loading in the picture.
img = cv.imread('images/faceimages/3.jpg')
cv.imshow('Image_Loaded', img)

# harcascasde do not bother about color of picture, so changing from BGR to Gray
gray = cv.cvtColor(img, code = cv.COLOR_BGR2GRAY) 
cv.imshow('Gray_Image', gray)

# loading the classifier
har_clf = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# detecting face
face_cordinates = har_clf.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors =3)

# number of faces detected
print(f'{len(face_cordinates)} faces detected in image')

# drawing rectangle on original image using the returned coordiantes of faces.
for (x,y,w,h) in face_cordinates:
    cv.rectangle(img= img, pt1=(x,y), pt2= (x+w, y+h), color= (0,255,150), thickness= 2)
cv.imshow(f'Detected faces : {len(face_cordinates)}', img)

cv.waitKey(0)

