import cv2

# Read the image
img = cv2.imread("flower.jpg")

# Convert the image to grayscale
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding
thresholdimg = cv2.threshold(grayimg, 180, 255, cv2.THRESH_BINARY)[1]

# Display the original and thresholded images
cv2.imshow("Original Image", img)
cv2.imshow("Thresholded Image", thresholdimg)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
