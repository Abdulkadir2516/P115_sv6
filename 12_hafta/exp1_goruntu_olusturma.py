import cv2 as cv
import numpy as np


resim = np.zeros((2000,2000,3),dtype="uint8")
s = 0
for i in range(500):
    x = s % 256
    s += 1
    for j in range(500):
        if i<256:
            resim[i,j] = [0,0,x] # BGR
        elif i<513:
            resim[i,j] = [0,x,255-x] # BGR


cv.imshow("dene", resim)
cv.waitKey()


