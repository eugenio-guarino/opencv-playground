import numpy as np
import cv2

# insert any image file you want here
img = cv2.imread('image.jpg')

# open window
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

# show image in window
cv2.imshow('Image', img)

cv2.imwrite("output.jpg", img)
print(img)

print(img.dtype)
print(img.shape)

# like console readline
cv2.waitKey()


