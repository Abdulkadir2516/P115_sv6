import cv2 as cv
import numpy as np

video = cv.VideoCapture("../src/rat.avi")#

while video.isOpened():
    _,frame = video.read(1)

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    _, tresh = cv.threshold(gray, 200,255, cv.THRESH_OTSU)


    if _:
        cv.imshow("threshold", tresh)

    if cv.waitKey(33) == ord("q"):
        break















