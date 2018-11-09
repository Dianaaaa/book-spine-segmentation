import cv2
import numpy as np


# 图像预处理（缩放、高斯滤波）
def pre_treatment(name):
    img = cv2.imread(name, 0)
    img2 = cv2.resize(img, (600, 450))
    img2 = cv2.GaussianBlur(img2, (3, 3), 0)
    return img2


def draw(img, theta, rho):
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return 0


img = pre_treatment('book1.jpg')
edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi/180, 160)  # 最后一个参数可调节，会影响直线检测的效果
lines1 = lines[:, 0, :]
result = img.copy()
houghlines = [];  # 存储检测出的垂直线
for rho, theta in lines1[:]:
    if (theta < (np.pi/9.0)) or (theta > (17*np.pi/9.0)):  # 限制与y轴夹角小于20度的线
        houghlines.append([rho, theta])
        draw(result, theta, rho)
print(len(houghlines))  # 得到竖直线的集合
cv2.imshow('result', result)
cv2.waitKey()
