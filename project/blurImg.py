import cv2
img=cv2.imread('flower.jpg')
gaussianimg=cv2.GaussianBlur(img,(41,41),0)
gaussianimg1=cv2.GaussianBlur(img,(41,41),10)
cv2.imshow("original",img)
cv2.imshow("GaussianBlur",gaussianimg)
cv2.imshow("GaussianBlur1",gaussianimg1)
