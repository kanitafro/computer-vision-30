import os
import cv2

# print("Current working directory:", os.getcwd())

img = cv2.imread(r'C:\Users\Korisnik\Downloads\cv\handwritten.png')
if img is None:
    print("Error: Image not found or invalid format!")
    exit()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# basic threshold
'''
ret, thresh80 = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)
ret, thresh127 = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
ret, thresh100 = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)
cv2.imshow('thresh80', thresh80)
cv2.imshow('thresh127', thresh127)
cv2.imshow('thresh100', thresh100)

# saving the files (optional)
try:
    cv2.imwrite('thresh80.png', thresh80) 
    #cv2.imwrite('thresh127.png', thresh27) 
    #cv2.imwrite('thresh100.png', thresh100) 
except:
    print("Couldn't save new file")
'''

# adaptive threshold
thresh1 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 81, 20)
thresh2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 20)

thresh3 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)
thresh4 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

'''
# saving the files (optional)
try:
    cv2.imwrite('thresh1.png', thresh1)
    cv2.imwrite('thresh2.png', thresh2)
    cv2.imwrite('thresh3.png', thresh3)
    cv2.imwrite('thresh4.png', thresh4)
except:
    print("Couldn't save new file")
'''

cv2.imshow('image', img)
cv2.imshow('thresh1', thresh1)
cv2.imshow('thresh2', thresh2)
cv2.imshow('thresh3', thresh3)
cv2.imshow('thresh4', thresh4)

cv2.waitKey(0)