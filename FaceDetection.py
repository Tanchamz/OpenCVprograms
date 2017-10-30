import numpy as np
import cv2

face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     #this file is available at repository
cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()

    if ret==True:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(gray,1.3,5)

        for(a,b,c,d)in faces:
            cv2.rectangle(img,(a,b),(a+c,b+d),(0,255,255),2)

        cv2.imshow('img',img)
        k=cv2.waitKey(30)&0xff

        if k==27:
            break

cap.release()
cv2.destroyAllWindows()
