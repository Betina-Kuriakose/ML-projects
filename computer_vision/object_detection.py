import imutils
import cv2
import time

cam=cv2.VideoCapture(0) 
time.sleep(1) #allow the camera to warm up, why, because the first few frames may be of lower quality
firstFrame=None #initializing the first frame to None
area=500 #minimum area size for motion detection
while True:
    _,img=cam.read()
    text="Unoccupied"
    grayimg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    grayimg=cv2.GaussianBlur(grayimg,(21,21),0)
    if firstFrame is None:
        firstFrame=grayimg
        continue
    imgDiff = cv2.absdiff(firstFrame,grayimg)
    thresh=cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]
    thresh=cv2.dilate(thresh,None,iterations=2)
    cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c)<area:
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        text="Occupied"
    print(text)
    cv2.putText(img,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
    cv2.imshow("Camera",img)
    key=cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()