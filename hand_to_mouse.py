# Organize imports

import pyautogui
import cv2
import imutils
import numpy as np

def overlaps(rect1, rect2):
    if(rect1[0] > rect2[2] or rect2[0] > rect1[2]):
        return False
    elif(rect1[3] < rect2[1] or rect2[3] < rect1[1]):
        return False
    else:
        return True


cap = cv2.VideoCapture(0)
SHOW_FEED = True

# Pre-trained haar cascades
palm_detector =cv2.CascadeClassifier("palm_haar_cascade.xml")
fist_detector =cv2.CascadeClassifier("fist_haar_cascade.xml")

feed_resolution = (480, 480)
screen_resolution = pyautogui.size()
prev_palm = None

def moveMouse(x,y):
    mouse_x =  (x * screen_resolution[0])/feed_resolution[0]
    mouse_y = (y * screen_resolution[1])/feed_resolution[1]
    pyautogui.moveTo(mouse_x, mouse_y) 

def clickMouse(x,y):
    mouse_x = screen_resolution[0] - (x * screen_resolution[0])/feed_resolution[0]
    mouse_y = (y * screen_resolution[1])/feed_resolution[1]
    pyautogui.click(mouse_x, mouse_y)


while True:
    try:
        ret, img = cap.read()  
        img = cv2.flip(img, 1)      
    except:
        print("Error! Cannot access webcam.")
        break      
    
    # Detect fists
    fists = fist_detector.detectMultiScale(img, scaleFactor = 1.05, minNeighbors=5)
    if fists is not None:
        for x, y, w, h in fists:
            # Red rectangles for fists
            img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,0,255),3)
            cv2.putText(img,"FIST", (x + int(w/4),y + int(h/2)),cv2.FONT_HERSHEY_SIMPLEX, 1.3,(0,0,255),2,cv2.LINE_AA)
            moveMouse(x + int(w/2),y + int(h/2))
    
    # Detect palms
    palms = palm_detector.detectMultiScale(img, scaleFactor = 1.03, minNeighbors=5)
    if palms is not None:
        for x, y, w, h in palms:
            curr_palm = (x, y, x+w, y+h)
            # There's a little extra code for this one because there were a lot of false positives showing up
            if prev_palm is None:
                prev_palm = curr_palm
            else:
                # Check for consecutive overlapping detections to ensure consistency 
                if overlaps(curr_palm, prev_palm):
                        # Green rectangles for palms
                    img = cv2.rectangle(img, (x,y), (x+w,y+h),(0,255,0),3)
                    cv2.putText(img,"PALM", (x + int(w/4),y + int(h/2)),cv2.FONT_HERSHEY_SIMPLEX, 1.3,(0,255,0),2,cv2.LINE_AA)
                    clickMouse(x + int(w/2),y + int(h/2))          
    else:
        prev_palm = None

    if SHOW_FEED:
        cv2.imshow('video', img)

    # Quit using the 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
