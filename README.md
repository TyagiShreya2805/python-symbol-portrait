# 🖼️ Python Symbol Portrait Generator

A computer vision and image processing project that converts a portrait into a symbol-based artwork using Python and OpenCV.

The project detects the face, preprocesses the image, converts it to grayscale, resizes it for rendering, and maps pixel brightness values to symbols to create a text-based portrait.

---

## ✨ Features

- Face detection using OpenCV Haar Cascades
- Automatic face cropping with configurable padding
- Image preprocessing
  - Grayscale conversion
  - Image resizing for symbol rendering
- ASCII symbol portrait generation
- HTML rendering for improved visualization
- Modular project architecture

---

## 📂 Project Structure

```
python-symbol-portrait/
│
├── input/
│   └── portrait.jpg
│
├── output/
│   ├── cropped_face.jpg
│   ├── grayscale_face.jpg
│   ├── symbol_portrait.txt
│   ├── symbol_portrait.html
│   └── .gitkeep
│
├── src/
│   ├── face_detector.py
│   ├── image_loader.py
│   ├── preprocessing.py
│   ├── renderer.py
│   └── symbol_mapper.py
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🔄 Processing Pipeline

```
Portrait Image
      │
      ▼
Load Image
      │
      ▼
Face Detection
      │
      ▼
Largest Face Selection
      │
      ▼
Face Cropping
      │
      ▼
Grayscale Conversion
      │
      ▼
Resize for Symbol Rendering
      │
      ▼
Brightness Mapping
      │
      ▼
ASCII Symbol Portrait
      │
      ▼
TXT + HTML Output
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/TyagiShreya2805/python-symbol-portrait.git
```

Move into the project

```bash
cd python-symbol-portrait
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Project

Place a portrait inside

```
input/portrait.jpg
```

Run

```bash
python3 app.py
```

Generated outputs will be available in

```
output/
```

---

## 🛠 Technologies Used

- Python 3.11
- OpenCV
- NumPy
- HTML
- Git & GitHub

---

## 📌 Current Status

Completed

- Image loading
- Face detection
- Face cropping
- Grayscale conversion
- Image resizing
- Symbol mapping
- Text rendering
- HTML rendering

In Progress

- Background removal
- Contrast enhancement
- Better symbol mapping
- Python-symbol rendering improvements

Planned

- Unicode rendering
- Emoji rendering
- PNG export
- CLI arguments
- Multiple rendering styles
- Performance optimization

---

## 📸 Example Workflow

```
Portrait

↓

Detected Face

↓

Cropped Face

↓

Grayscale

↓

ASCII Portrait

↓

HTML Preview
```

---

## 📄 License

This project is licensed under the MIT License.

## Author

Shreya Tyagi