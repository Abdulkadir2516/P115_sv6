import cv2 as cv

video = cv.VideoCapture("../src/video.mp4")

while True:

    _, frame = video.read()

    if _:
        cv.imshow("video",frame)


    if cv.waitKey(30) == ord("q"):
        break




