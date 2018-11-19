import cv2
import numpy as np

img_width = 600
img_height = 450


# 图像预处理（缩放、高斯滤波）
def pre_process(name):
    img = cv2.imread(name, 0)
    img_resized = cv2.resize(img, (img_width, img_height))
    img_gau = cv2.GaussianBlur(img_resized, (3, 3), 0)
    return img_resized, img_gau


def draw(img, lines):
    for rho, theta in lines[:]:
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


def draw_vertical(img, lines):
    for rho, theta in lines[:]:
        x1 = rho
        x2 = rho
        y1 = 0
        y2 = img_width
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
    return 0


def line_sifting(lines_list):
    lines = []
    for rho, theta in lines_list[:]:
        if (theta < (np.pi / 9.0)) or (theta > (17 * np.pi / 9.0)):  # 限制与y轴夹角小于20度的线
            lines.append([rho, theta])
    lines.sort()
    i = 0
    j = 0
    lines_final = []
    while i < len(lines)-1:
        if j >= len(lines)-1:
            break
        j = i + 1
        lines_final.append(lines[i])
        while j < len(lines)-1:
            if lines[j][0]-lines[i][0] > 10:
                i = j
                break
            else:
                j = j+1
    return lines_final


def main():
    img_show, img = pre_process('book1.jpg')
    edges = cv2.Canny(img, 50, 150, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi/180, 140)  # 最后一个参数可调节，会影响直线检测的效果
    lines1 = lines[:, 0, :]
    # result = img.copy()
    houghlines = line_sifting(lines1)  # 存储并筛选检测出的垂直线
    draw_vertical(img_show, houghlines)
    print(houghlines)
    cv2.imshow('result', img_show)
    cv2.waitKey()


main()

