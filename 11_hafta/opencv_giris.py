import cv2 as cv

print(cv.__version__)

resim = cv.imread("./src/manzara.jpg")

print(type(resim))
print(resim.shape)
print(resim.ndim)

cv.imshow("resim" , resim)

cv.waitKey()








