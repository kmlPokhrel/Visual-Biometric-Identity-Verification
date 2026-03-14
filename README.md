<!-- PROJECT BANNER -->

<p align="center">

<h1 align="center">🛡️ Visual Biometric Identity Verification</h1>
<h3 align="center">Computer Vision Pipeline for Real-Time Facial Attribute Recognition</h3>

<p align="center">
A computer vision system that converts raw facial image data into biometric predictions using classical machine learning techniques.
</p>

<p align="center">
<img src="https://img.shields.io/badge/python-3.9.18-blue.svg">
<img src="https://img.shields.io/badge/framework-Flask-black.svg">
<img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-green.svg">
<img src="https://img.shields.io/badge/ML-PCA%20%7C%20SVM-orange.svg">
<img src="https://img.shields.io/badge/Deployment-Railway-lightgrey.svg">
<img src="https://img.shields.io/badge/status-Active-success.svg">
</p>

</p>

---

# 🚀 System Overview

**Visual Biometric Identity Verification** is a full-stack computer vision project that analyzes facial images and extracts biometric features through a structured machine learning pipeline.

The system processes images in real time and performs:

• Face detection  
• Image preprocessing  
• Feature extraction using PCA (Eigenfaces)  
• Classification using Support Vector Machine  

The goal of this project is to demonstrate a **complete computer vision pipeline**, from raw image acquisition to final prediction output.

---

# 🧠 Vision Processing Pipeline

<p align="center">

INPUT IMAGE  
    ⬇  
Face Detection (Haar Cascade)  
    ⬇  
Image Preprocessing  
    ⬇  
Eigenface Feature Extraction (PCA)  
    ⬇  
Support Vector Machine Classification  
    ⬇  
Prediction Output  

</p>

---

# 🖥️ Live System Demonstration

### System Interface

<p align="center">
<img src="static/logo.png" width="400">
</p>

<p align="center">
<i>Vision Analytics interface used for biometric prediction.</i>
</p>

---

### Neural Pipeline in Action

<p align="center">
  <a href="static/demo.mp4">
    <img src="static/demo_thumbnail.png" width="650">
  </a>
</p>

<p align="center">
<i>Click the image to watch the demo video.</i>
</p>

<p align="center">
<i>Real-time facial ROI detection followed by PCA projection and SVM classification.</i>
</p>

---

# 🧬 Core System Architecture

The system processes facial images through a **four-stage analysis pipeline**.
## System Architecture

<p align="center">
  <img src="./static/architecture.png" width="800">
</p>
---

## 1️⃣ Face Detection

• Implemented using **Haar Cascade Classifiers**  
• Detects facial regions in input frames  
• Extracts the **Region of Interest (ROI)** for analysis  

---

## 2️⃣ Image Preprocessing

• Converts RGB images into **grayscale format**  
• Resizes images to **100 × 100 resolution**  
• Normalizes input data to improve model consistency  

---

## 3️⃣ Feature Extraction (Eigenfaces)

• Uses **Principal Component Analysis (PCA)**  
• Reduces image dimensionality  
• Projects facial features into **Eigenface space**  

This step captures the most important facial variance patterns.

---

## 4️⃣ Classification

• Feature vectors are passed to a **Support Vector Machine (SVM)**  
• The trained classifier predicts biometric attributes  
• Inference is performed in **near real time**

---

# 📚 Dataset

The model was trained using a dataset containing facial images captured under different lighting conditions and orientations.

Before training, images were:

• Converted to grayscale  
• Resized to 100 × 100 pixels  
• Flattened into feature vectors  

PCA was then applied to extract the most significant facial components before classification.

---

# ⚙️ Technology Stack

| Layer | Technology |
|------|------|
| Computer Vision | OpenCV |
| Feature Extraction | PCA (Eigenfaces) |
| Classification | Support Vector Machine |
| Backend | Flask |
| Deployment | Railway |
| Runtime | Python 3.9 |

---

# 📊 Model Performance

| Metric | Score | Description |
|------|------|------|
| Accuracy | 85–92% | Prediction accuracy across test samples |
| Inference Time | <120 ms | Near real-time prediction |
| Dimensional Reduction | 95% variance retained | PCA compression efficiency |

---

# 📁 Project Structure

```
Visual-Biometric-Identity-Verification
│
├── app
│   ├── face_recognition.py
│   └── views.py
│
├── model
│   ├── model_svm.pickle
│   ├── pca_dict.pickle
│   └── haarcascade.xml
│
├── templates
│
├── static
│   ├── images
│   └── logo.png
│
├── main.py
├── Procfile
└── requirements.txt
```

---

# 💻 Local Setup

Clone the repository

```
git clone https://github.com/kmlPokhrel/Visual-Biometric-Identity-Verification.git
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows

```
.\venv\Scripts\activate
```

Linux / macOS

```
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run application

```
python main.py
```

---

# 🌐 Deployment Architecture

The application is deployed using **Railway cloud infrastructure**.

• Flask application served using **Gunicorn**  
• Optimized OpenCV build using **opencv-python-headless**  
• Environment versions locked for reproducibility  

Environment versions:

Python 3.9.18  
scikit-learn 0.24.2

---

# 🔮 Future Improvements

Planned improvements for the system include:

### Identity Recognition
Link Eigenface signatures to registered user profiles.

### Liveness Detection
Detect spoofing attempts such as printed photos.

### Emotion Analysis
Integrate facial emotion recognition models.

### Multi-Person Recognition
Expand system to support larger identity datasets.

---

# 👨‍💻 Developer

**Kamal Pokhrel**

Computer Vision • Machine Learning • ML Engineering

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the project  
📢 Share with the community

---

<p align="center">
Built using classical computer vision and machine learning techniques.
</p>
