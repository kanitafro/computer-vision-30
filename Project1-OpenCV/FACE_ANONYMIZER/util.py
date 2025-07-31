import cv2
import mediapipe as mp

def process_image(img, face_detection):
    H, W, _ = img.shape

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)
    #print(out.detections) # will print out the data we need to know what to extract
    
    if out.detections is not None: # makes sure there IS a face in the image
        for detection in out.detections:
            location_data = detection.location_data
            bbox = location_data.relative_bounding_box

            xmin, ymin, width, height = bbox.xmin, bbox.ymin, bbox.width, bbox.height
            xmin = int(xmin * W) # xmin + width of image
            ymin = int(ymin * H) # xmin + height of image
            width = int(width * W) 
            height = int(height * H) 
            
            # draw rectangle to show detected face (optional)
            border_width = 6
            OFFSET = (border_width+1)//2
            #img = cv2.rectangle(img, (xmin-OFFSET, ymin-OFFSET), (xmin+width+OFFSET, ymin+height+OFFSET), (0, 255, 0), border_width)
            
            #blur faces
            ratio_h = 1 # default is 1 (e.g. 2//5 if you want to blur only the eyes)
            ratio_w = 1 # default is 1 (e.g. 1//5 if you want to blur only the left side of the face)
            img[ymin:ymin+height*ratio_h, xmin:xmin+width*ratio_w, :] = cv2.blur(img[ymin:ymin+height*ratio_h, xmin:xmin+width*ratio_w, :], (80, 80))
    
    return img

    
