import cv2
import imutils
img=cv2.imread('flower.jpg')
resized=imutils.resize(img,width=200)
cv2.imshow('OriginalImage.jpg',img)
cv2.imshow('resized.jpg',resized)
cv2.imwrite('resizedimg.jpg',resized)
