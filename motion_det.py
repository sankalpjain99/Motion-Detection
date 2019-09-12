
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
if cap.isOpened():
    ret,frame1 = cap.read()
    ret,frame2 = cap.read()
else:
    ret=False
    
while(ret):
    d = cv2.absdiff(frame1,frame2)
    grey=cv2.cvtColor(d,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(5,5),0)
    ret,th = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dil = cv2.dilate(th,np.ones((3,3),np.uint8),iterations=2)
    er = cv2.erode(th,np.ones((3,3),np.uint8),iterations=2)
    cont,hier = cv2.findContours(dil,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame1,cont,-1,(0,0,255),1)
    
    cv2.imshow("Original",frame2)
    cv2.imshow("Output",frame1)
    if cv2.waitKey(1)==27:
        break
    frame1=frame2
    ret,frame2 = cap.read()
cv2.destroyAllWindows()
cap.release()
