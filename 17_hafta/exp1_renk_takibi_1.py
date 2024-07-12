import cv2 as cv
import numpy as np

video = cv.VideoCapture("../src/video.mp4")#"../src/video.mp4"

while video.isOpened():
    _,frame = video.read(1)
    h,w,_ = frame.shape
    for i in range(h):
        for j in range(w):
            if frame[i,j][0] > 170 and frame[i,j][1] > 120 and  frame[i,j][2] < 50 :
                frame[i, j] = [255,255,255]
            else:
                frame[i, j] = [0,0,0]
    if _:
        cv.imshow("video", frame)

    if cv.waitKey(33) == ord("q"):
        break
#
# frame = cv.imread("../src/img.png")
# h, w, _ = frame.shape
#
# for i in range(h):
#     for j in range(w):
#         if frame[i,j][0] > 170 and frame[i,j][1] > 120 and  frame[i,j][2] < 50 :
#             frame[i, j] = [255,255,255]
#         else:
#             frame[i, j] = [0,0,0]
# cv.imshow("video", frame)
#
# cv.waitKey()
# cv.destroyAllWindows()







