import cv2
import numpy as np
cap = cv2.VideoCapture(0)
sas, img = cap.read()

cv2.imwrite("arkaplan.jpg", img)

background=cv2.imread("arkaplan.jpg")
background = cv2.resize(background, (800, 800))

while True:

    sas ,img =cap.read()

    img=cv2.resize(img,(800,800))
    #aynı boyuta esitliyoruz
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 0, 200])
    upper = np.array([180, 50, 255])

    mask = cv2.inRange(imgHSV, lower, upper)

    img[np.where(mask == 255)] = background[np.where(mask == 255)]
    cv2.imshow("img", img)
    #cv2.imshow("mask", mask)

    cv2.waitKey(1)