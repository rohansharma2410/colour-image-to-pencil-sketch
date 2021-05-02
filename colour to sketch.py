import cv2
image = cv2.imread("C:/Users/Rohan Sharma/Downloads/download.jfif")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


inverted_image = 255 - gray_image

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

cv2.imshow("original image", image)
cv2.imshow("pencil sketch", pencil_sketch)
cv2.waitKey(0)