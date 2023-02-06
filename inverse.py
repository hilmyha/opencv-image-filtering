import numpy as np
import cv2
from cv2 import imread

# read image
img_src = cv2.imread('UTS\image\captured_img.png', 0)

scale_percent = 20
width = int(img_src.shape[1] * scale_percent / 15)
height = int(img_src.shape[0] * scale_percent / 15)
img_size = (width, height)

img = cv2.resize(img_src, img_size, interpolation=cv2.INTER_AREA)

kernel = np.ones((14, 14), np.uint8)

thresh = 70

imgbinary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
imginvers = ~imgbinary

imgdilation = cv2.dilate(img, kernel, iterations=1)

# flt_img = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)

cv2.imshow('IPF', imginvers)
cv2.waitKey(0)
cv2.destroyAllWindows()
