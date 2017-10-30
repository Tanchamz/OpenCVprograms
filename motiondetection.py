import numpy 
import cv2

def diffImg(t0,t1,t2):
    d1=cv2.absdiff(t2,t1)
    d2=cv2.absdiff(t1,t0)
    return cv2.bitwise_and(d1,d2)

cam=cv2.VideoCapture(0)

while True:
    ret,frame=cam.read()
    tminus=cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
    t=cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
    tplus=cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)

    tminus=t
    t=tplus
    tplus=cv2.cvtColor(cam.read()[1],cv2.COLOR_BGR2GRAY)
    cv2.imshow("movement indicator",diffImg(tminus,t,tplus))
    k=cv2.waitKey(5)& 0xff

    if k==27:
        break

cv2.release()
cv2.destroyAllWindows()
