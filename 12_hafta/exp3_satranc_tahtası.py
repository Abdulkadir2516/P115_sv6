import cv2 as cv
import numpy as np

tahta = np.zeros((800,800,3), dtype="uint8")

for i in range(8):
    for j in range(8):
        if i % 2 ==0 and j%2==0:
            tahta[100*i:100*(i+1), 100*j:100*(j+1)]= [np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)]
        elif i % 2 !=0 and j%2!=0:
            tahta[100*i:100*(i+1), 100*j:100*(j+1)]= [np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)]
        else:
            tahta[100*i:100*(i+1), 100*j:100*(j+1)]= [np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)]


cv.imshow("dene", tahta)
cv.waitKey()

