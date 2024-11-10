# src/frame_selection.py

import os
import shutil
import cv2
import numpy as np
from sklearn.cluster import KMeans

def select_frames_by_scene_segmentation(frames, num_frames=20, output_folder="frames/selected_frames"):
    # Ensure the output folder exists and is clean
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)  # Clear previous selected frames

    # A simple histogram-based scene segmentation technique
    selected_frames = []
    hist_diffs = []

    for i in range(1, len(frames)):
        prev_frame = cv2.imread(frames[i - 1], cv2.IMREAD_GRAYSCALE)
        curr_frame = cv2.imread(frames[i], cv2.IMREAD_GRAYSCALE)

        hist_diff = cv2.compareHist(
            cv2.calcHist([prev_frame], [0], None, [256], [0, 256]),
            cv2.calcHist([curr_frame], [0], None, [256], [0, 256]),
            cv2.HISTCMP_CORREL
        )
        hist_diffs.append((frames[i], hist_diff))

    hist_diffs.sort(key=lambda x: x[1])
    selected_frames = [frame for frame, _ in hist_diffs[:num_frames]]

    for frame_path in selected_frames:
        frame_name = os.path.basename(frame_path)
        selected_frame_path = os.path.join(output_folder, frame_name)
        shutil.copy(frame_path, selected_frame_path)

    return selected_frames

def select_frames_by_kmeans(frames, num_clusters=20, output_folder="frames/selected_frames"):

    # Ensure the output folder exists and is clean
    os.makedirs(output_folder, exist_ok=True)
    for file in os.listdir(output_folder):
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            os.unlink(file_path)  # Clear previous selected frames

    feature_vectors = []
    for frame in frames:
        img = cv2.imread(frame)
        img = cv2.resize(img, (100, 100))  # Resize to reduce computation
        feature_vectors.append(img.flatten())

    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    kmeans.fit(feature_vectors)
    cluster_centers = kmeans.cluster_centers_

    selected_frames = []
    for center in cluster_centers:
        distances = [np.linalg.norm(feature - center) for feature in feature_vectors]
        selected_frames.append(frames[np.argmin(distances)])
    
    for frame_path in selected_frames:
        frame_name = os.path.basename(frame_path)
        selected_frame_path = os.path.join(output_folder, frame_name)
        shutil.copy(frame_path, selected_frame_path)

    return selected_frames
