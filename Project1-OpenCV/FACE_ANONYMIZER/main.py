import cv2
import os
import argparse
import mediapipe as mp
from util import process_image

args = argparse.ArgumentParser()
args.add_argument("--mode", default='video') # image, video, or webcam
args.add_argument("--filePath", default='./testvideo.mp4') # None if args.mode in ["webcam"]
    
args = args.parse_args()

output_dir = './output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

########## detect faces ##########
mp_face_detection = mp.solutions.face_detection
with mp_face_detection.FaceDetection(min_detection_confidence=0.5, model_selection=0) as face_detection:
    # model 0 is for faces within 2m from the camera, model 1 within 5m
        
    # read
    if args.mode in ["image"]:
        img = cv2.imread(args.filePath)
        if img is None:
            print("Error: Image not found or invalid format!")
            exit()

        img = process_image(img, face_detection)

        cv2.imwrite(os.path.join(output_dir, 'output.png'), img)
            
        ########## show ##########
        cv2.imshow('img', img)
        cv2.waitKey(0)

    elif args.mode in ["video"]:

        cap = cv2.VideoCapture(args.filePath)
        ret, frame = cap.read()

        output_video = cv2.VideoWriter(os.path.join(output_dir, 'output.mp4'),
                                        cv2.VideoWriter_fourcc(*'MP4V'),
                                        25,
                                        (frame.shape[1], frame.shape[0]))

        while ret:
            frame = process_image(frame, face_detection)
        
            output_video.write(frame)
            ret, frame = cap.read()
        cap.release()
        output_video.release()

    elif args.mode in ["webcam"]:
        cap = cv2.VideoCapture(0)  # 0 = default webcam
            
        while True: # going through frames
            ret, frame = cap.read()
            frame = process_image(frame, face_detection)
            cv2.imshow('webcam', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
                break

