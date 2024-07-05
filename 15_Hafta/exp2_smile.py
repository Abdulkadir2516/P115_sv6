import cv2 as cv
import numpy as np

smile = cv.imread("../src/smile.png")

cv.imshow("smile", smile[50:700,250:1200])

smile = np.zeros((600,1000,3),dtype="uint8")
smile[::,::] = [255,255,255]

cv.rectangle(smile,(20,20),(960,560),(0,255,0),20, lineType=cv.LINE_AA)
cv.circle(smile,(300,150),80,[255,0,0],-1)
cv.circle(smile,(300,150),80,[0,0,0],3)
cv.circle(smile,(700,150),80,[255,0,0],-1)
cv.circle(smile,(700,150),80,[0,0,0],3)

# Üçgenin köşe noktalarını tanımla
points = np.array([[500,200],[550,300],[450,300]])

cv.ellipse(smile, (500,400), (50,300), 90,0,360, (255,0,0), thickness=5 )

cv.putText(smile, "Hello world", (400,420), color=(255,0,0), fontFace=1, fontScale=3, thickness=3)
# Üçgeni çiz
cv.polylines(smile, [points], isClosed=True, color=(0, 255, 0), thickness=3)

cv.imshow("smile2", smile)




cv.waitKey()