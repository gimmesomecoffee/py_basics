import cv2

img = cv2.imread("galaxy.jpg", 8)

cv2.imshow("Galaxy", img)
cv2.waitKey(0)
print(img)