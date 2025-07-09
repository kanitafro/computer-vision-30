import os
import cv2

#print(os.path.exists('yellow_flowers.jpg'))
img = cv2.imread('yellow_flowers.jpg')
if img is None:
    print("Error: Image not found or invalid format!")
    exit()

# convert from BGR colorspace to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.imshow('image', img_rgb)
cv2.waitKey(0)