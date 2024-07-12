import cv2 as cv
import numpy as np

video = cv.VideoCapture(1)#"../src/video.mp4"

lower_white = np.array([75, 100, 100])
upper_white = np.array([130, 255, 255])

while video.isOpened():
    _,frame = video.read(1)

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    mask = cv.inRange(hsv, lower_white, upper_white)
    cv.imshow("mask", mask)

    if _:
        cv.imshow("video", frame)

    if cv.waitKey(33) == ord("q"):
        break















