import os
import cv2

img = cv2.imread('tall_flower.jpg')
if img is None:
    print("Error: Image not found or invalid format!")
    exit()

#normal blur
k_size = 33
img_blur = cv2.blur(img, (k_size, k_size))

# gaussian blur
img_gaussian = cv2.GaussianBlur(img, (k_size, k_size), 5) # additional parameter

# median blur
img_median = cv2.medianBlur(img, k_size)

cv2.imshow('image', img)
cv2.imshow('blurred image', img_blur)
cv2.imshow('gaussian blur image', img_gaussian)
cv2.imshow('median blur image', img_median)

cv2.waitKey(0)
