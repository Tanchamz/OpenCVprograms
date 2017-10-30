import numpy as np
import cv2

img_bgr=cv2.imread('<location of image>')
img gray=cv2.cvtColor(img_bgr,cv2.COLOR_BGR2GRAY)

template=cv2.imread('<location of template>',0)
w,h=template.shape[::-1]

result=cv2.matchTemplate(img gray,template,cv2.TM_NORMED)
threshold=0.6
location=np.where(result>=threshold)

for pt in zip(*location)
    cv2.rectangle(img bgr,pt,(pt[0]+w,pt[1]+h),(0,250,250),2)

cv2.imshow('detected',img bgr)
cv2.waitKey(0)
