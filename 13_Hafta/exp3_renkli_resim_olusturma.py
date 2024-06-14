import cv2 as cv
import numpy as np

img = np.zeros((127*6,255*6,3), dtype="uint8")
renk = 0
for i in range(img.shape[1]):
    if renk % 255 == 0:
        renk = 0
    renk+=1

    if i<255*1:
        img[::,i] = [0,renk,255]
    elif i<255*2:
        img[::,i] = [0,255,255-renk]
    elif i<255*3:
        img[::,i] = [renk,255,0]
    elif i<255*4:
        img[::,i] = [255,255-renk,0]
    elif i<255*5:
        img[::,i] = [255,0,renk]
    elif i<255*6:
        img[::,i] = [255-renk,0,255]



cv.imshow("img",img)

cv.waitKey()