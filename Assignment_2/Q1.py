import cv2

img=cv2.imread('1713054_ccn_IA2.PNG')
x,y,z= img.shape

cv2.line(img, (0,0),(y,x),(0,255,0), 4)
cv2.imshow("frame",img)
cv2.waitKey(0)