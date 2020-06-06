import cv2
import time
start_time=time.time()
cap= cv2.VideoCapture(0)

while True:
    end_time=time.time()
    diff=int(end_time-start_time)
    x, frame= cap.read()
    vertically_flipped= cv2.flip(frame,-1)
    print(diff)
    if diff%5==0:
        cv2.imshow("Frame",vertically_flipped)
    else:
        cv2.imshow("Frame",frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break 