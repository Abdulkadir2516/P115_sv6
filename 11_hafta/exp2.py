import cv2 as cv

resim = cv.imread("./src/manzara.jpg")

# rgb değil bgr
resim2 = resim.copy()
resim3 = resim.copy()
resim4 = resim.copy()

x,y,_= resim.shape

for i in range(x):
    for j in range(y):
        resim2[i,j][0] = 0
        resim3[i,j][1] = 0
        resim4[i,j][2] = 0

cv.imshow("resim renkli1", resim)
cv.imshow("resim renkli2", resim2)
cv.imshow("resim renkli3", resim3)
cv.imshow("resim renkli", resim4)

cv.waitKey()
