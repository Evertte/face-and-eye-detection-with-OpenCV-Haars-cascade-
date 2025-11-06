# Eyes Detection with OpenCV (Haar Cascades)

A lightweight **eyes-only** detector using OpenCV.  
It first detects a **face**, then searches for **eyes only in the upper part of the face** (Region of Interest) and applies simple geometry filters to reduce false positives (ears, blinds, etc.).

https is not required (desktop app), runs locally via Python + OpenCV.

---

## ✨ Features
- CPU-only, real-time eyes detection
- Face → upper-half ROI → eyes (fewer false positives)
- Tunable parameters: `scaleFactor`, `minNeighbors`, min/max eye size
- Optional stricter model: `haarcascade_eye_tree_eyeglasses.xml`
- Works with your laptop webcam (`VideoCapture(0)`)

---

## 📦 Requirements
- Python 3.8+
- OpenCV 4.x

Install:
```bash
pip install opencv-python
```

🔧 How it works (high level)

Read a frame from webcam

Convert to grayscale and optionally equalize histogram for contrast

Detect faces on the full frame

For each face:

Crop an upper-half ROI

Run eye cascade in that ROI

Filter boxes by aspect ratio, size, and vertical band

Pick the best pair (aligned and spaced reasonably)
