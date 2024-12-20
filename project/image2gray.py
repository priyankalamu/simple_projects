import cv2
image=cv2.imread("flower.jpg")
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('original',image)
cv2.imshow('Gray',gray)
cv2.imwrite('graynew.jpg',gray)
print(image.shape)
print(image.size)