import cv2 as cv
import numpy as np


resim = np.zeros((500,500,3),dtype="uint8")

x,y,d = resim.shape

for i in range(500):
    resim[200:300,245:255] = [255,255,255]
    resim[245:255,200:300] = [255,255,255]

cv.circle(resim, center=(int(x/2),int(y/2)), radius=50,color=[255,0,0],thickness=5)

cv.imshow("dene", resim)
cv.waitKey()


