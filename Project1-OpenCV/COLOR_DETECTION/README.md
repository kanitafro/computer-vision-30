# Color Detection Mini-Project

The purpose of this mini-project was to detect the color yellow using only OpenCV operations.  
![Image](https://github.com/user-attachments/assets/ada9a342-49de-46b9-ba95-2f7ea285d614)

The crucial part here is the ***get_limits(color)*** function from `util.py` which gets the lower and upper limits whose purpose is to "slice" the hue wheel:

<img width="288" height="270" alt="Image" src="https://github.com/user-attachments/assets/05c7ba68-0cbb-4058-9c4e-3f0dbe1648e6" />

At the very beginning of `main.py` we defined the color we want, in this case it's yellow and we define it as (0, 255, 255) in BGR colorspace as *"pure yellow"*. Then when the webcam is on, each frame is first converted to the HSV colorspace, then after getting the limits from ***get_limits()*** they are used to get the mask. If we visualize the mask, this is how it behaves when yellow is detected:

<div align="center" style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px;">
  <img src="./demo/webcam_normal.png" width="45%" alt="Input" style="border: 1px solid #eee">
  <img src="./demo/webcam_mask.png" width="45%" alt="Output" style="border: 1px solid #eee">
</div>

As you can see, it detects in traces the yellow of the furniture in the background, it's not perfect but it does the trick. To finish, we just draw the rectangle from the detected bounding box. It works pretty well, even works with transparent yellow water bottle after struggling with it for a little while.

![Image](https://github.com/user-attachments/assets/b7167c57-1267-4062-be29-7c177b67c1c0)
