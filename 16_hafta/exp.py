# resim üzerinde fare ile resim kırpma
# farenın koordinatını resim üzerinde gösterme

import cv2 as cv
resim = cv.imread("../src/manzara2.jpg")

bas_x , bas_y = 0,0
def fare_olayları(event, x,y, flag, userdata):

    global bas_x,bas_y
    if event == cv.EVENT_MOUSEMOVE:
        print(f"x = {x}, y= {y}")
        a = resim.copy()

        cv.putText(a, f"x = {x}, y= {y}", (50, 50), color=(255, 0, 0), fontFace=1, fontScale=3, thickness=3)
        cv.imshow("dene", a)

    if event == cv.EVENT_LBUTTONDOWN:
        bas_x = x
        bas_y = y

    if event == cv.EVENT_LBUTTONUP:
        cv.imshow("kirpilmis", resim[bas_y:y,bas_x:x ])

        cv.imwrite("../src/kirpilmis.jpg", resim[bas_y:y,bas_x:x ])


cv.imshow("dene", resim)
print(resim.shape)
# cv.imshow("ev", resim[170:230,250:380])

cv.setMouseCallback("dene", fare_olayları)


if cv.waitKey() == ord("q"):
    cv.destroyAllWindows()
