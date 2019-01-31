import cv2
import numpy as np
count=0
truck_cascade0 = cv2.CascadeClassifier('data/cascade.xml')
'''
#truck_cascade1 = cv2.CascadeClassifier('data1/cascade.xml')

truck_cascade2 = cv2.CascadeClassifier('data2/cascade.xml')

truck_cascade3 = cv2.CascadeClassifier('data3/cascade.xml')
truck_cascade4 = cv2.CascadeClassifier('data4/cascade.xml')
truck_cascade5 = cv2.CascadeClassifier('data5/cascade.xml')
truck_cascade6 = cv2.CascadeClassifier('data6/cascade.xml')
truck_cascade7 = cv2.CascadeClassifier('data7/cascade.xml')
truck_cascade8 = cv2.CascadeClassifier('data8/cascade.xml')
'''
cap = cv2.VideoCapture(0)
c=0
while True:
    
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    trucks0 = truck_cascade0.detectMultiScale(gray, 50, 50)
    cv2.line(img,(1000,150),(50,150),(100,100,0),2)
    '''
    #trucks1 = truck_cascade1.detectMultiScale(gray, 50, 50)

    trucks2 = truck_cascade2.detectMultiScale(gray, 50, 50)
    
    trucks3 = truck_cascade3.detectMultiScale(gray, 50, 50)
    trucks4 = truck_cascade4.detectMultiScale(gray, 50, 50)
    trucks5 = truck_cascade5.detectMultiScale(gray, 50, 50)
    trucks6 = truck_cascade6.detectMultiScale(gray, 50, 50)
    trucks7 = truck_cascade7.detectMultiScale(gray, 50, 50)
    trucks8 = truck_cascade8.detectMultiScale(gray, 50, 50)
    '''
    
    for(x,y,w,h) in trucks0:
        #print("truck at ("+str(x),str(y)+")" )
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 255, 0), 2)
        if(not(c%50==0)):
            if(y>150 and y<165 ):
                count=count+1
    '''
    for(x,y,w,h) in trucks1:
        print("truck at ("+str(x),str(y)+")" )
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 255, 0), 2)
    
    for(x,y,w,h) in trucks2:
        print("truck at ("+str(x),str(y)+")" )
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 255, 0), 2)
    
    for(x,y,w,h) in trucks3:
        print("truck at ("+str(x),str(y)+")" )
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 255, 0), 2)
    for(x,y,w,h) in trucks4:
        print("truck at ("+str(x),str(y)+")" )
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 255, 0), 2)
    for(x,y,w,h) in trucks5:
        print("truck at ("+str(x),str(y)+")" )
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 255, 0), 2)
    for(x,y,w,h) in trucks6:
        print("truck at ("+str(x),str(y)+")" )
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 255, 0), 2)
    for(x,y,w,h) in trucks7:
        print("truck at ("+str(x),str(y)+")" )
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 255, 0), 2)

    for(x,y,w,h) in trucks8:
        print("truck at ("+str(x),str(y)+")" )
        cv2.rectangle(img, (x,y),(x+w, y+h), (255, 255, 0), 2)
    '''
    c=c+1
    print(str(c))
    cv2.putText(img,"count:" + str(count) ,(10,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    cv2.imshow('img',img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    # k = cv2.waitKey(30) & 0xff
    #if k == 27:
    #   break

cap.release()
cv2.destroyAllWindows()