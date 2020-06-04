import cv2
cap=cv2.VideoCapture(0)
i=0
n=int(input('enter number of frames after which you want the image to be inverted\n'))
while True:
    x, frame= cap.read()
    flipped= cv2.flip(frame,-1)
    if i<n:
        cv2.imshow('image',frame)
        i+=1
    else:
        cv2.imshow('image',flipped)
    if cv2.waitKey(1000) & 0xFF==ord('q'):
        break