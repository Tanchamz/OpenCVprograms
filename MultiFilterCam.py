import numpy as np
import cv2
cam=cv2.VideoCapture(0)
while True :
    ret,frame=cam.read()
    laplacian=cv2.Laplacian(frame,cv2.CV_64F)
    sobelx=cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely=cv2.Sobel(frame,cv2.CV_64F,0,1,ksize=5)
    edges=cv2.Canny(frame,100,100)
    cv2.imshow('Original',frame)
    cv2.imshow('sobelx',sobelx)
    cv2.imshow('sobely',sobely)
    cv2.imshow('laplacian',laplacian)
    cv2.imshow('canny',edges)
    k=cv2.waitKey(5)& 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()
