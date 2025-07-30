# PROJECT 1 - OpenCV Tutorial

Learning basic operations with images and video using the ***opencv-python*** library.
Based on [OpenCV tutorial for beginners | FULL COURSE in 3 hours with Python](https://youtu.be/eDIj5LuIL4A?si=gaCR-mjeaJiWvLNn) by *Computer vision engineer*. The video is used as a guideline to learn OpenCV, not copy and paste everything mentioned in the video. ***Will later go through the ["OpenCV bootcamp"](https://opencv.org/university/free-opencv-course/?utm_source=opcvu&utm_medium=menu&utm_campaign=obc) course that OpenCV offers for free and add the work here***.

In `demo` folder you can find all images that are saved by running the respective Python files (as listed in the README of `demo`).
The folder `fig` stores images used in this README, they're not obtained by running any code.

### Prerequisites for Running the Code

First, install OpenCV locally by running `pip install opencv-python` on the terminal. The library that's used in the code is called **cv2**, thus when importing libraries, indicate `import cv2` at the top.

### Overview of the Provided Python Files

* `cv_image_operations.py` goes through the basic operations with images using the `cv2` library. The demo is done on the *image3.jpg* in this folder and uses the function *`show_coordinates`* from the `helper_functions1.py`. The operations done in this code are reading, writing, and showing the image, as well as cropping and resizing.

* `colorspaces.py` experiments with a few different color representations and the demo is done on the *yellow_flower.jpg* image. Running this code will save 3 files: *yellow_flower_rgb.jpg*, *yellow_flower_gray.jpg*, and *yellow_flower_hsv.jpg*.

* `blurring.py` works with 3 basic blur functions—blur, gaussian blurr, and median blur. The demo is done on *tall_flower.py* and it isn't set to save any additional files when running the code.

* `threshold.py` uses *handwritten.png* as demo image and shows differences between using regular thresshold and adaptive threshold.

* `edge_detection.py` detects edges in an image and shows how to manipulate the thickness (and with it, their clarity) of the edges using *sophia_katseye.jpg* as the demo image.

* `drawing.py` shows how to draw a line, a rectangle, a circle, and how to put text on *whiteboard.png* demo image taken from Google with a search for "whiteboard". 

---
## Notes and Analysis

### Blurring

Important note about specifying the kernel size: cv2.GaussianBlur() and cv2.medianBlur() require the kernel size (k_size) to be a positive odd number (e.g., 3, 5, 7, etc.). For cv2.blur() kernel size can be any integer, even though it's a standard to use odd integer.
Visual comparison between `blur`, `GaussianBlur`, and `medianBlur`. Kernel size (k_size) is set to 33, the third parameter in gaussian blur is set to 5. These are the outputs with the given parameters:

#### **Original vs blur**  

![Original image vs blurred with normal blur](./fig/blurring_normalvblur.png)

#### **blur vs GaussianBlur**  

![Image blurred with normal blur vs with gaussian blur](./fig/blurring_blurvgaussian.png)

#### **blur vs medianBlur**  

![Image blurred with normal blur vs with median blur](./fig/blurring_blurvmedian.png)

---
### Threshold

The image used here was `handwritten.png`. The provided code has a commented region where basic threshold was used and here's what it looks like with different values of threshold (80, 100, 127):

![Implementing basic threshold](./fig/thresh80_100_127.png)

Since the basic threshold doesn't do well on slight lighting changes in the image, adaptive threshold is more suitable for this. The `adaptiveThreshold` function is used to apply adaptive thresholding to an image, which is particularly useful when lighting conditions vary across the image like we have in this case. Explanation of the parameters:

             cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C)

* `src` is the input image in grayscale (it has to be in a singe channel)
  
* `maxValue` is the value assigned to pixels that satisfy the threshold condition (e.g., if a pixel value is above the threshold, it will be set to maxValue.
  
* `adaptiveMethod`: the method used was Adaptive Threshold Gaussian. There are 2 types of adaptive methods:
  1. `cv2.ADAPTIVE_THRESH_MEAN_C`: The threshold is the mean of the neighborhood area
  2. `cv2.ADAPTIVE_THRESH_GAUSSIAN_C`: The threshold is a weighted sum of the neighborhood values, where weights are from a Gaussian window
  
* `thresholdType` is the type of thresholding to apply. Common options:
  1. cv2.THRESH_BINARY: dst(x, y) = maxValue if src(x, y)>T(x, y) else 0
  2. cv2.THRESH_BINARY_INV: dst(x, y) = 0 if src(x, y)>T(x, y) else maxValue  

  Here, T(x, y) is the dynamically computed threshold for the pixel.

* `blockSize` is the size of the neighborhood (odd integer > 1) used to compute the threshold for each pixel. A larger block size means the threshold is computed over a larger area, which can smooth out local variations but may lose finer details.
* `C` is a constant subtracted from the computed threshold (can be positive, negative, or zero). This is used to fine-tune the threshold value. A higher C makes the threshold more "lenient," resulting in more pixels being classified as foreground.

#### **Higher C, different block sizes**

* thresh1 (blockSize=81) computes the threshold over a much larger neighborhood, making it less sensitive to local variations but potentially missing finer details. 
* thresh2 (blockSize=21) is more sensitive to local changes but may introduce more noise.

![Comparison between parameters](./fig/threshold_thresh1_2.png)

#### **Low C, different block sizes**

Since C is much smaller here, the threshold is less adjusted, resulting in a stricter binarization.

* thresh3 (blockSize=31) is smoother
* thresh4 (blockSize=11) preserves more details but also retains more noise.
  
![Comparison between parameters](./fig/threshold_thresh3_4.png)

---
### Edge Detection

#### Comparing the original with examples of higher minVal
* Example 1: minVal = 100, maxVal = 200  
* Example 2: minVal = 200, maxVal = 500
![Comparison between parameters 1 and 2](./fig/sophia_edges_1_2.png)

#### Comparing the original with examples of lower minVal
* Example 1: minVal = 20, maxVal = 40  
* Example 2: minVal = 20, maxVal = 400
* Example 3: minVal = 10, maxVal = 100
![Comparison between parameters 3, 4, and 5](./fig/sophia_edges_3_5.png)

#### Dilate vs Erode

Function `cv2.dilate` makes the edges thicker and `cv.erode` makes edges thinner. The functions use Numpy ones matrices where the default value is `np.ones(1, 1)` and by dilating (eroding) with `np.ones(x, x)` the edges become thicker (thinner) by x times. Blow is the example of using x=3 for both dilate and erode. Dilate uses the original image and erode uses the dilated image, thus the dimensions go back to (1, 1).

![Dilate and erode functions](./fig/sophia_dilate_erode.png)

---
### Drawing

#### Line
Drawing the line requires the x,y coordinates of the starting point, then the coordn+inates of the end point, color, and the thickness of the line. This is a green line starting at point (213, 481) and ending at (786, 132) with thickness 3.
 
      img_line = cv2.line(img, (213, 481), (786, 132), (0, 255, 0), 3)


#### Rectangle
The rectangle requires the coordinates of the top-left corner and bottom-right corner, the collor of the edge, and thickness of the edge. If you want to fill the rectangle with the provided color then an additional parameter is required—just put in -1. This will be a blue rectangle whose upper left corner is at (213, 481) and bottom right corner at (786, 132) with thickness 3.

      img_rectangle = cv2.rectangle(img, (213, 481), (786, 132), (255, 0, 0), 3) # last parameter is -1 if you want to fill it

#### Circle
Drawing a circle requires the coordinates of its center and length of its radius in pixels, as well as the color of the circle. This will be a filled red circle whose center is in point (356, 233) and radius 50. Note that it's BGR notation and not RGB notation.

      img_circle = cv2.circle(img, (356, 233), 50, (0, 0, 255), -1) # filled circle

#### Text
To have text on the image, you need to specify the coordinates, the font, size of the text, color of the text, and thickness.

      cv2.putText(img, 'Hellou', (459, 392), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 0), 2)

This is how everything looks put together:
![Drawings on the whiteboard](./fig/whiteboard_drawings.png)
---
### Contours

At first, when making bounding boxes, I made a mistake to which coordinates of the corners of the rectangle to use.

      x1, y1, x2, y2 = cv2.boundingRect(cnt)
      cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
This is how the bounding boxes turned out:
![Flock bounding boxes incorrect placement](./fig/flock_boundingboxes_incorrect.png)

Then I changed the last 2 parameters to w (width) and h (height) and added them up for the 

![Flock bounding boxes correct placement](./fig/flock_boundingboxes.png)
