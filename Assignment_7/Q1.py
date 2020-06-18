import cv2
import numpy as np
cap= cv2.VideoCapture(0)
cv2.namedWindow('frame')
def nothing(x):
    pass
cv2.createTrackbar('H','frame',0,180,nothing)
cv2.createTrackbar('HH','frame',255,180,nothing)
cv2.createTrackbar('S','frame',0,255,nothing)
cv2.createTrackbar('HS','frame',255,255,nothing)
cv2.createTrackbar('V','frame',0,255,nothing)
cv2.createTrackbar('HV','frame',255,255,nothing)
while True:
    x,frame=cap.read()
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    h=cv2.getTrackbarPos('H','frame')
    hh=cv2.getTrackbarPos('HH','frame')
    s=cv2.getTrackbarPos('S','frame')
    hs=cv2.getTrackbarPos('HS','frame')
    v=cv2.getTrackbarPos('V','frame')
    hv=cv2.getTrackbarPos('HV','frame')
    lower_bound=np.array([h,s,v])
    upper_bound=np.array([hh,hs,hv])
    mask=cv2.inRange(hsv_frame,lower_bound,upper_bound)
    colored_mask=cv2.bitwise_and(frame,frame,mask=mask)

    contours, heirarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    areas=[cv2.contourArea(c) for c in contours]
    max_index=np.argmax(areas)
    max_contour=contours[max_index]
    cv2.drawContours(frame,[max_contour],-1,(0,255,0),5)

    cv2.imshow('frame',frame)
    cv2.imshow('hsv',colored_mask)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break