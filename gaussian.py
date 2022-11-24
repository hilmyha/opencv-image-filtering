import cv2
import numpy as np

img_src = cv2.imread('UTS\image\img_example.jpg')

scale_percent = 20
width = int(img_src.shape[1] * scale_percent / 100)
height = int(img_src.shape[0] * scale_percent / 100)
img_size = (width, height)

img = cv2.resize(img_src, img_size, interpolation=cv2.INTER_AREA)

flt_img = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0, sigmaY=0)

cv2.imshow('GAUSSIAN', flt_img)
cv2.waitKey(0)
cv2.destroyAllWindows()