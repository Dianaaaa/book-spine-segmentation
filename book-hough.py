import cv2
import numpy as np

# 图片
img = cv2.imread('book1.jpg')
img2 = cv2.resize(img, (600, 450))
cv2.imshow('book', img2)
cv2.waitKey()
edges = cv2.Canny(img2, 50, 150, apertureSize=3)
cv2.imshow('canny', edges)
cv2.waitKey()

