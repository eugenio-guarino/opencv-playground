import numpy as np
import cv2

img = cv2.imread('cat.jpg', 0)
cv2.imshow('Original', img)

ret, thresh_basic = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
cv2.imshow('Basic binary', thresh_basic)

thresh_adapt = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Adapt binary', thresh_adapt)

cv2.waitKey(0)
cv2.destroyAllWindows()
