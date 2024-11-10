# main.py
from src.frame_extraction import extract_frames
from src.frame_selection import select_frames_by_scene_segmentation, select_frames_by_kmeans
from src.object_detection import load_detection_model, detect_objects_on_frames
from src.evaluate import evaluate_detection

def main():
    video_path = "data/input_video.mp4"
    output_folder = "frames/extracted_frames"

    # Extract frames
    frames = extract_frames(video_path, output_folder, frame_rate=15)
    
    if not frames:
        print("No frames were extracted. Please check the video file and frame extraction function.")
        return

    # Select frames using scene segmentation or clustering
    # selected_frames = select_frames_by_scene_segmentation(frames)  
    # or 
    selected_frames = select_frames_by_kmeans(frames)
    
    # Load detection model
    model = load_detection_model()

    # Detect objects in selected frames
    detected_frames = detect_objects_on_frames(selected_frames, model)

    # Evaluate
    evaluate_detection(detected_frames)

if __name__ == "__main__":
    main()
