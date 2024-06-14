import cv2 as cv
import numpy as np

img = cv.imread("../src/rengarenk.png")

cv.imshow("oiginal_resim", img)

img2 = np.zeros(img.shape, dtype="uint8")

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        if img[i,j][0] == 255 or img[i,j][2] == 255:
            img2[i,j] = img[i,j]


cv.imshow("görnütü", img2)

cv.waitKey()