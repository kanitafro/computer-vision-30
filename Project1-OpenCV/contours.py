import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from helper_functions1 import setup_mouse_callback_binary
# print("Current working directory:", os.getcwd())

img = cv2.imread(os.path.join('.', 'flock.png'))
if img is None:
    print("Error: Image not found or invalid format!")
    exit()
#img = cv2.resize(img, (img.shape[1]*2//3, img.shape[0]*2//3))

###### Contours ######

# getting a binary image
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('thresh', thresh)

# using 4.11.0.86 opencv-python (type 'pip show opencv-python' into terminal)
# -> using 2 parameters
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# contour is a closed border of each white region

for cnt in contours:
    print(cv2.contourArea(cnt))
    cv2.drawContours(img, cnt, -1, (0, 255, 0), 1) #draws contours
    # now drawing bounding boxes
    x1, y1, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

'''
In our case, all the birds are clearly separated and more or less
the same size, printing out the contours shows that they range from
~450 to ~1100. If there are some very small contours, for example <100
then we can consider them as noise and remove them by having this
line inside the loop:
    if cv2.contourArea(cnt) > 100
        print(cv2.contourArea(cnt)) # or whatever you want in here

This ensures we don't detect noise in the image.
'''

######################


####### Displaying image with coordinates and RBG values #######

# Option 1: Create a window and set up the mouse callback (using helper_functions1.py)
'''# calling setup_mouse_callback_binary from helper_functions1.py
window_name = 'Image Viewer'
cv2.namedWindow(window_name)
setup_mouse_callback_binary(window_name, thresh)
'''

# Option 2: using matplotlib to get zoom as well
'''# use plt.imshow to use get zoom and coordinates + channels of each pixel
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
'''
################################################################

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()