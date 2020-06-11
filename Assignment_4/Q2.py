import cv2
import numpy as np 

img = cv2.imread('1713054_ccn_IA2.PNG')
image=img.copy()
pts=[]
def mouse(event,x,y,flags,param):
    if event== cv2.EVENT_LBUTTONDOWN:
        pts.append((x,y))
        print(x,y)
        print(pts)
    if len(pts)==2:
        imgg=image[pts[0][1]:pts[1][1],pts[0][0]:pts[1][0]]
        cv2.imshow("Cropped",imgg)
cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse)
cv2.imshow('img',img)
cv2.waitKey(0)