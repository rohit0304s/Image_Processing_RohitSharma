import cv2
import numpy as np 

iimg=cv2.imread('IMG_3879.jpg')
img=cv2.resize(iimg,(640,640))
image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel=np.ones((2,2))
gaussian_blur=cv2.GaussianBlur(image,(5,5),2)
edge=cv2.Canny(gaussian_blur,150,200)
contours,heirarchy=cv2.findContours(edge,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
areas=[cv2.contourArea(c) for c in contours]
max_index=np.argmax(areas)
max_contour=contours[max_index]

perimeter=cv2.arcLength(max_contour,True)
ROI=cv2.approxPolyDP(max_contour,0.01*perimeter,True)
cv2.drawContours(img,[ROI],-1,(0,255,0),2)

pts_1=np.array([ROI[0],ROI[1],ROI[3],ROI[2]],np.float32)
pts_2=np.array([(0,0),(500,0),(0,500),(500,500)],np.float32)
perspective=cv2.getPerspectiveTransform(pts_1,pts_2)
transformed=cv2.warpPerspective(img,perspective,(500,500))

cv2.imshow('img',img)
cv2.imshow('tramsformed',transformed)
cv2.waitKey(0)