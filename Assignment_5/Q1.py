import cv2
import numpy as np

cap=cv2.VideoCapture(0)

pts=[]
def mouse(event,x,y,flags,param):
    counter=0
    if event==cv2.EVENT_LBUTTONDOWN:
        if counter == 0:
            counter+=1
            cv2.imwrite('img.jpg',frame)
            
        pts.append((x,y))

while True:
    x,frame=cap.read()
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame',mouse)
    img=cv2.imread('img.jpg')
    if len(pts)==2:
        img_cropped=img[pts[0][1]:pts[1][1],pts[0][0]:pts[1][0]]
        cv2.imshow('cropped',img_cropped)
        template_gray=cv2.cvtColor(img_cropped,cv2.COLOR_BGR2GRAY)
        width=img_cropped.shape[1]
        height=img_cropped.shape[0]
    
        img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        res=cv2.matchTemplate(img_gray,template_gray,cv2.TM_CCOEFF_NORMED)
        loc=np.where(res>=0.9)
        
        for x,y in zip(*loc[::-1]):
            cv2.rectangle(frame,(x,y),(x+height,y+width),(0,255,0),1)
            cv2.putText(frame,'OBJECT',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break