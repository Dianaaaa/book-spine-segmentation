import cv2
import numpy as np

img = cv2.imread('book1.jpg',0)
img2 = cv2.resize(img, (600, 450))
img2 = cv2.GaussianBlur(img2,(3,3),0)
edges = cv2.Canny(img2, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 160)
lines1 = lines[:, 0, :]
result = img2.copy()
for rho, theta in lines1[:]:
    if (theta < (np.pi/9.0)) or (theta > (17*np.pi/9.0)):
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        cv2.line(result, (x1, y1), (x2, y2), (255, 0, 0), 2)
cv2.imshow('result', result)
cv2.waitKey()
