import cv2
import numpy as np 
img= cv2.imread('IMG_3879.jpg')
iimg=cv2.resize(img,(640,640))
img_gray=cv2.cvtColor(iimg,cv2.COLOR_BGR2GRAY)

kernel=np.ones((2,2))
gaussian_blur=cv2.GaussianBlur(img_gray,(5,5),2)
canny=cv2.Canny(gaussian_blur,180,255)
gaussian_thresh=cv2.adaptiveThreshold(canny,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,5,1)

gau=cv2.subtract(255,gaussian_thresh)
erosion=cv2.erode(gau,kernel)
cv2.imshow('img',iimg)
cv2.imshow('Final image',erosion)
cv2.waitKey(0)