# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:44:44 2020

@author: ruba
"""

import cv2
face_mask = cv2.CascadeClassifier('cascade.xml')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    _, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = face_mask.detectMultiScale(gray,1.3,4)
    for(x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color=img[y:y+h, x:x+w]
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Using Mask',(55,280),font,0.5,(255,0,0))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Without Mask',(20,200),
                    font,0.5,(255,255,255))
        cv2.imshow('test',img)
 #the window will close when we press q
    if cv2.waitKey(1) & 0xFF ==ord('q'):
     break

cap.release()
cv2.destroyAllWindows()