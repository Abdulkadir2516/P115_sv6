import cv2 as cv

cam = cv.VideoCapture(0)

while cam.isOpened():

    ref, frame = cam.read()

    cv.imshow("pencere", frame)

    if cv.waitKey(33) == ord("q"):
        break

    # frame2 = cv.cvtColor(frame, cv.COLOR_BGR2GRAY) # gri görüntü
    # frame2 = cv.cvtColor(frame, cv.CALIB_CB_NORMALIZE_IMAGE)
    # frame2 = frame[::-1]
    # frame2 = frame[::,::-1]
    # frame2 = cv.flip(frame, 1)
    frame2 = cv.rotate(frame, 1)
    cv.imshow("pencere2", frame2)

