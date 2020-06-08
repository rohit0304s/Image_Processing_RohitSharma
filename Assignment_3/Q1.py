import cv2
import numpy as np 

img=cv2.imread("1713054_ccn_IA2.PNG")
x,y,z=img.shape

nx=x//7
ny=y//7
a=0
b=0
while(a<=x):
    b=0
    while(b<=y):
        color= [np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)]
        cv2.rectangle(img, (a,b), (a+nx,b+ny),color,-1)
        b+=ny
    a+=nx
cv2.imshow('Frame',img)
cv2.waitKey(0)
