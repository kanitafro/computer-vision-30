import os
import cv2
import numpy as np

img = cv2.imread(os.path.join('.', 'sophia_katseye.jpg'))
if img is None:
    print("Error: Image not found or invalid format!")
    exit()
img = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

###### Edge Detection Operations ######

img_edge1 = cv2.Canny(img, 100, 200) # minVal and maxVal
img_edge2 = cv2.Canny(img, 200, 500)
img_edge3 = cv2.Canny(img, 20, 40)
img_edge4 = cv2.Canny(img, 20, 400)
img_edge5 = cv2.Canny(img, 10, 100)

# using dilate to make the edges "thicker"
img_dilate = cv2.dilate(img_edge1, np.ones((3, 3), dtype = np.int8))

# erode is the opposite of dilate
img_erode = cv2.erode(img_dilate, np.ones((3, 3), dtype = np.int8))

cv2.imshow('image', img)
cv2.imshow('image_edge1', img_edge1)
#cv2.imshow('image_edge2', img_edge2)
#cv2.imshow('image_edge3', img_edge3)
#cv2.imshow('image_edge4', img_edge4)
#cv2.imshow('image_edge5', img_edge5)
cv2.imshow('image_dilate', img_dilate)
cv2.imshow('image_erode', img_erode)
cv2.waitKey(0)
