import os
import cv2
from helper_functions import show_coordinates

### Original image ###
img = cv2.imread('image3.jpg')
print(img.shape)
#cv2.imshow('image', img)

### Resizing image - to half the size while keeping proportions ###
width, height, channels = img.shape
resized_img = cv2.resize(img, (height//2, width//2)) # you first indicate height then width when resizing
print(resized_img.shape)
#cv2.imshow('image', resized_img)

##### Cropping image #####

#cv2.imwrite('cropped_image3.jpg', cropped_img) # save the copy of the cropped + resized image

cropped_img = img[:, 50:750] # indicate height then width]


#cropped_w, cropped_h, cropped_ch = cropped_img.shape
#cropped_img = cv2.resize(cropped_img, (cropped_h//2, cropped_w//2))
resized_img = cv2.resize(cropped_img, (cropped_img.shape[1]//2, cropped_img.shape[0]//2)) # this is the same as the 2 lines above
print("Cropped image size:", resized_img.shape)

# Set up the window and callback
window_name = 'Cropped and resized image'  # Can be any unique name
cv2.namedWindow(window_name)

# Pass the image and window name as parameters via 'param'
cv2.setMouseCallback(window_name, show_coordinates, {'image': resized_img, 'window_name': window_name})

# Initial display
cv2.imshow(window_name, resized_img)

cv2.waitKey(0)