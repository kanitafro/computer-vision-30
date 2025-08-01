import cv2
from PIL import Image
from util import get_limits

yellow = [0, 255, 255] # yellow in BGR 

cap = cv2.VideoCapture(0)  # 0 = default webcam
while True: # going through frames
    ret, frame = cap.read()
    
    hsvImage = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit = get_limits(color=yellow)
    mask = cv2.inRange(hsvImage, lowerLimit, upperLimit)

    mask_ = Image.fromarray(mask)
    bbox = mask_.getbbox()

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 3)

    #print(bbox)
    
    cv2.imshow('Webcam', frame)
    #cv2.imshow('Webcam', mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
