import cv2

resim =cv2.imread("../src/RGB-CMYK.png")

mavi = resim[:, :, 0] # mavi renk kanalını oku
cv2.imshow("mavi", mavi)
cv2.waitKey(0)
