import cv2
import numpy as np

def get_limits(color):
    c = np.uint8([[color]]) # here insert the bgr values which you want to convert to hsv
    hsvC = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hsvC[0][0][0] - 13, 100, 100
    upperLimit = hsvC[0][0][0] + 13, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit