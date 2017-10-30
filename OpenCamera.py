import numpy as np
import cv2

cam=cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()

    if ret==True:
        cv2.imshow('Original',frame)
        k=cv2.waitKey(5)& 0xFF

        if k==27:
            break

cap.release()
cv2.destroyAllWindows()
