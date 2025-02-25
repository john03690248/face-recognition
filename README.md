# Face Recognition with Haar Cascade and LBPH

This project implements a real-time face detection and recognition system using OpenCV. It utilizes **Haar Cascade Classifier** for face detection and **Local Binary Patterns Histograms (LBPH)** for face recognition. This system is designed to work on **Raspberry Pi**.

## Features

- **Real-time face detection** using Haar Cascade
- **Face recognition** using LBPH
- **Training and storing face data** for recognition
- **Supports multiple users** with labeled datasets
- **Works with live video feed** (webcam or Raspberry Pi camera module)

## Installation

### Prerequisites

Ensure you have Python installed along with the following dependencies:

```bash
pip install opencv-python opencv-contrib-python numpy
```

For Raspberry Pi, install OpenCV with:

```bash
sudo apt update
sudo apt install python3-opencv
```

### Clone the Repository

```bash
git clone https://github.com/john03690248/Face-Recognition.git
cd Face-Recognition
```

## Usage

### Run Face Detection and Recognition

To detect and recognize faces using a webcam or Raspberry Pi camera:

```bash
python main.py
```

If a known face is detected, the system will display the recognized name.

## Acknowledgments

- OpenCV for computer vision functions
- Haar Cascade for face detection
- LBPH for face recognition

