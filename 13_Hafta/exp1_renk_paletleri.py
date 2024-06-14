import cv2 as cv

img = cv.imread("../src/rengarenk.png")

cv.imshow("orjinal_görüntü",img)

img2 = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img3 = cv.cvtColor(img, cv.COLOR_HSV2BGR)

cv.imshow("gri_görüntü", img2)
cv.imshow("gri_görüntü", img3)

cv.waitKey()
