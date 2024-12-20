import cv2
img=cv2.imread("flower.jpg")
cv2.imshow('Lotus',img)
cv2.imwrite('flowers.jpeg',img)
cv2.waitKey(10000)
cv2.destroyAllWindows()
