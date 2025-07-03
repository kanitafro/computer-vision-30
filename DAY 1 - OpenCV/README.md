# DAY 1 - OpenCV tutorial

Learning basic operations with images and video using the ***opencv-python*** library.
Based on [OpenCV tutorial for beginners | FULL COURSE in 3 hours with Python](https://youtu.be/eDIj5LuIL4A?si=gaCR-mjeaJiWvLNn) by *Computer vision engineer*. The video is used as a guideline to learn OpenCV, not copy and paste everything mentioned in the video.

`cv_image_operations.py` goes through the basic operations with images using the `cv2` library. The demo is done on the *image3.jpg* in this folder and uses the function *`show_coordinates`* from the `helper_functions1.py`. The operations done in this code are reading, writing, and showing the image, as well as cropping and resizing.

`colorspaces.py` experiments with a few different color representations and the demo is done on the *yellow_flower.jpg* image. Running this code will save 3 files: *yellow_flower_rgb.jpg*, *yellow_flower_gray.jpg*, and *yellow_flower_hsv.jpg*.

### Prerequisites for running the code

First, install OpenCV locally by running `pip install opencv-python` on the terminal. The library that's used in the code is called **cv2**, thus when importing libraries, indicate `import cv2` at the top.
