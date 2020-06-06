import cv2

cap= cv2.VideoCapture(0)
counter=0
while True:
    x, frame= cap.read()
    counter+=1
    cv2.imshow("Frame", frame)
    cv2.imwrite('IMG_'+str(counter) + '.jpg', frame)

    if cv2.waitKey(1000) & 0xFF==ord('q'):
        break