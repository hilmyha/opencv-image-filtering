import cv2
import numpy as np

img_src = cv2.imread('image\captured_img.png')

scale_percent = 20
width = int(img_src.shape[1] * scale_percent / 15)
height = int(img_src.shape[0] * scale_percent / 15)
img_size = (width, height)

img = cv2.resize(img_src, img_size, interpolation=cv2.INTER_AREA)

flt_img = cv2.GaussianBlur(src=img, ksize=(5,5), sigmaX=0, sigmaY=0)

cv2.imshow('GAUSSIAN', flt_img)
cv2.waitKey(0)
cv2.destroyAllWindows()