import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([R,G,B])        #specify lower and upper values for colours that you want visible in image
    upper_red=np.array([R,G,B])
    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('res',res)
    k=cv2.waitKey(5)& 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
