import cv2 as cv

video = cv.VideoCapture(1)

while True:

    _, frame = video.read()

    if _:
        cv.imshow("kamera",frame)

    if cv.waitKey(30) == ord("q"):
        break

    if cv.waitKey(30) == ord("s"):
        cv.imwrite(filename="./deneme.jpg", img=frame)




