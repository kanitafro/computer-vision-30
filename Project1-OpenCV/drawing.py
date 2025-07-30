import os
import cv2
import numpy as np
from helper_functions1 import setup_mouse_callback

# print("Current working directory:", os.getcwd())

img = cv2.imread(os.path.join('.', 'whiteboard.png'))
if img is None:
    print("Error: Image not found or invalid format!")
    exit()
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

###### Drawing Operations ######
# have in mind that it's BGR notation not RGB

# green line starting at point (213, 481) and ending at (786, 132) with thickness 3
img_line = cv2.line(img, (213, 481), (786, 132), (0, 255, 0), 3)

# blue rectangle whose upper left corner is at (213, 481) and bottom right corner at (786, 132) with thickness 3
img_line_rectangle = cv2.rectangle(img, (213, 481), (786, 132), (255, 0, 0), 3) # last parameter is -1 if you want to fill it

# circle
img_line_rectange_circle = cv2.circle(img, (356, 233), 50, (0, 0, 255), -1)

# text
cv2.putText(img, 'Hellou', (459, 392), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)

#################

# Create a window and set up the mouse callback
window_name = 'Image Viewer'
cv2.namedWindow(window_name)
setup_mouse_callback(window_name, img)

# Wait for a key press to exit
cv2.waitKey(0)
cv2.destroyAllWindows()
