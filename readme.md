# Shoppin

This project aims to detect shoppable items in a 60-second video by selecting a subset of frames (around 20 out of 900) and running object detection on them. The focus is on optimizing computational time and ensuring high accuracy.

## Table of Contents

- [Objective](#objective)
- [Challenges](#challenges)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Implementation Details](#implementation-details)
- [Evaluation](#evaluation)
- [Troubleshooting](#troubleshooting)

---

## Objective

The goal is to reduce the total number of frames from a 60-second video (900 frames at 15 FPS) to around 20 frames, then perform object detection on these selected frames to identify shoppable items efficiently.

## Challenges

- Extracting meaningful frames from the video to minimize redundancy.
- Applying techniques such as scene segmentation, optical flow analysis, and clustering to select frames with minimal computational resources.
- Ensuring high detection accuracy while reducing the number of frames processed.

---

## Project Structure

```plaintext
shoppable_item_detection/
├── data/
│   └── videos/              # Folder for storing videos
├── frames/
│   └── selected_frames/     # Folder for storing selected frames
├── models/
│   └── object_detection/    # Folder for storing or downloading pre-trained models
├── src/
│   ├── frame_extraction.py  # Code to extract frames from video
│   ├── frame_selection.py   # Code for selecting optimal frames
│   ├── object_detection.py  # Code to run object detection on frames
│   └── evaluate.py          # Code to evaluate the performance
├── requirements.txt         # Python packages required for the project
└── main.py                  # Main file to execute the complete pipeline
```

## Installation

1. Clone this repository and navigate to the project directory:

   ```plaintext
   git clone https://github.com/Devyadav0512/shopping_items_extractor.git
   cd shopping_items_extractor
   ```
2. Set up a virtual environment (recommended):

   ```plaintext
   # Create a virtual environment
   python3 -m venv venv

   # Activate the virtual environment
   # For Windows
   source venv/Scripts/activate
   # For macOS/Linux
   source venv/bin/activate
   ```
3. Install the required packages:

   ```plaintext
   pip install -r requirements.txt
   ```
4. **Download Pretrained Model** (if not using TorchVision models):

   * Place any downloaded pretrained models in `models/object_detection/`.

---

## Usage

1. **Add a Sample Video** : Place a sample video in `data/videos/` and name it, for example, `input_video.mp4`. Make sure the file path in `main.py` matches the video filename.
2. **Run the Project** : Execute the main pipeline with:

   ```plaintext
   python main.py
   ```

    This will:

* Extract frames from the video.
* Select a subset of frames using scene segmentation or k-means clustering.
* Run object detection on the selected frames.
* Output evaluation metrics, such as average detection confidence and execution time.

1. **Results** :

* Selected frames will be stored in `frames/selected_frames/`.
* Detection metrics will display in the terminal.

---

## Implementation Details

### 1. **Frame Extraction (`frame_extraction.py`)**

* Extracts frames from the video at a specified frame rate using OpenCV.

### 2. **Frame Selection (`frame_selection.py`)**

* Techniques for frame selection:
  * **Scene Segmentation** : Selects frames based on histogram differences.
  * **K-means Clustering** : Groups visually similar frames and selects representative frames from each cluster.

### 3. **Object Detection (`object_detection.py`)**

* Uses a pre-trained model (e.g., Faster R-CNN from TorchVision) to detect objects in each selected frame.

### 4. **Evaluation (`evaluate.py`)**

* Evaluates detection accuracy, speed, and computational efficiency of the selected frames.

---

## Evaluation

* **Accuracy** : Measures the effectiveness of detecting shoppable items.
* **Speed** : Calculates the time taken to process the selected frames.
* **Computational Efficiency** : Compares the selected frames versus all frames in terms of resource use.

---

## Troubleshooting

1. **CUDA Compatibility (for GPU)** : If you have a GPU, ensure CUDA is installed and that you have a compatible PyTorch version. Check the [PyTorch installation page]() for CUDA-compatible installation.
2. **Memory Issues** : If you encounter memory issues, consider reducing the frame rate in `extract_frames` or optimizing code to clear unused frames from memory.

---

## Contributing

Feel free to submit issues or pull requests if you’d like to improve this project!

---

## License

This project is licensed under the MIT License - see the [LICENSE]() file for details.

```plaintext
### Additional Notes

- Make sure to replace `https://github.com/Devyadav0512/shopping_items_extractor.git` with the actual repository URL if you’re hosting this on GitHub.
- This `README.md` includes comprehensive instructions for setting up and running the project, along with troubleshooting tips and implementation details.
```
