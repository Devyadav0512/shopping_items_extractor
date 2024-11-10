# src/frame_extraction.py

import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=15):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print(f"Error: Couldn't open video {video_path}")
        return []

    # Get video properties
    total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"Total frames in video: {total_frames}")
    
    frames = []
    frame_count = 0
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Only save the frame if it matches the FPS we are interested in
        # if frame_count % int(video_capture.get(cv2.CAP_PROP_FPS)) == 0:
        frame_path = os.path.join(output_folder, f"frame_{frame_count}.jpg")
        cv2.imwrite(frame_path, frame)
        frames.append(frame_path)
        print(f"Extracted frame: {frame_path}")  # Debugging line

        frame_count += 1

    video_capture.release()
    print(f"Extracted {len(frames)} frames.")
    return frames
