import cv2 as cv

smile = cv.imread("../src/smile.png")

cv.imshow("smile", smile[50:700,250:1200])

cv.waitKey()