import cv2
import numpy as np 

img=cv2.imread("1713054_ccn_IA2.PNG")
x,y,z=img.shape

nx=x//7
ny=y//7
a=0
b=0
counter=0
while(a<=y):
    counter+=1
    while(b<=x and b>=0):
        color= [np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)]
        if counter%2!=0:
            cv2.rectangle(img, (b,a), (b+nx,a+ny),color,-1)
            b+=nx
            cv2.waitKey(500)
            cv2.imshow('Frame',img)
            img=cv2.imread("1713054_ccn_IA2.PNG")
        else:
            cv2.rectangle(img, (b,a), (b+nx,a+ny),color,-1)
            b-=nx
            cv2.waitKey(500)
            cv2.imshow('Frame',img)
            img=cv2.imread("1713054_ccn_IA2.PNG")
    if counter%2!=0:
        b-=nx
    else:
        b=0
    a+=ny
cv2.imshow('Frame',img)
cv2.waitKey(0)