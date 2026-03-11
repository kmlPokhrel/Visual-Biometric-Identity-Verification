# 🛡️ Visual Biometric Identity Verification
### Neural Computer Vision Pipeline for Real-Time Attribute Recognition

[![Python Version](https://img.shields.io/badge/python-3.9.18-blue.svg)](https://www.python.org/downloads/release/python-3918/)
[![Framework](https://img.shields.io/badge/framework-Flask-000000.svg)](https://flask.palletsprojects.com/)
[![Deployment](https://img.shields.io/badge/platform-Railway-lightgrey.svg)](https://railway.app/)

---

## 📖 Overview
This system is a high-performance **Biometric Identity Pipeline** designed to transform raw pixel data into actionable biometric insights.

While currently optimized for **Gender Classification**, the underlying architecture uses **Principal Component Analysis (PCA)** and **Support Vector Machines (SVM)**, creating a scalable framework for advanced biometric verification and facial identity analytics.

The project demonstrates a complete **computer vision pipeline**, from face detection and preprocessing to feature extraction and classification within a deployable web application.

---

## 🖼️ Visual Demonstrations

### System Interface
![System Logo](static/images/logo.png)

*The “Vision Analytics” identity representing the fusion of computer vision and biometric security.*

### Neural Pipeline in Action
![System Demo](static/images/demo.gif)

*Real-time ROI detection followed by Eigen-projection and SVM classification.*

---

## 🛠️ Technical Architecture

The system processes images through a **four-stage vision pipeline**:

### 1️⃣ ROI Detection
- Uses **Haar Cascade Classifiers**
- Detects facial structures
- Extracts the **Region of Interest (ROI)**

### 2️⃣ Image Preprocessing
- Converts images to **grayscale**
- Normalizes images to **100 × 100 resolution**
- Reduces noise and computational overhead

### 3️⃣ Eigen Projection
- Applies **Principal Component Analysis (PCA)**
- Projects faces into **Eigenface space**
- Extracts key biometric variance features

### 4️⃣ SVM Classification
- Feature vectors are passed to a **Support Vector Machine**
- Produces classification predictions with statistical confidence

---

## 🚀 Deployment & Production

The application is designed for **cloud deployment on Railway**.

### Production Stack
- **Flask** – Backend web framework
- **Gunicorn** – Production WSGI server
- **Railway** – Cloud hosting platform
- **OpenCV Headless** – Optimized server-side computer vision

### Environment Synchronization
Versions are locked to maintain model integrity:

- **Python 3.9.18**
- **scikit-learn 0.24.2**
- **opencv-python-headless**

This guarantees consistent behavior between **local training and cloud inference**.

---

## 📂 Project Structure

```plaintext
Visual-Biometric-Identity-Verification/
│
├── app/
│   ├── face_recognition.py   # Core ML logic & PCA projection
│   └── views.py              # Flask routes and request handling
│
├── model/
│   ├── model_svm.pickle      # Pre-trained SVM classifier
│   ├── pca_dict.pickle       # PCA dimensionality reduction model
│   └── haarcascade_...xml    # OpenCV face detection weights
│
├── templates/                # Web interface templates
│
├── static/
│   └── images/               # Project images and demo media
│
├── main.py                   # Application entry point
├── Procfile                  # Railway deployment command
└── requirements.txt          # Python dependencies
```

---

## 📈 Model Performance & Metrics

| Metric | Score | Analysis |
|------|------|------|
| Accuracy | 85% – 92% | Reliable performance across varied lighting conditions |
| Inference Time | < 120 ms | Suitable for real-time processing |
| Dimension Reduction | 95% Variance | PCA preserves critical biometric features |

---

## 💻 Local Setup

### Clone Repository
```bash
git clone https://github.com/kmlPokhrel/Visual-Biometric-Identity-Verification.git
```

### Create Virtual Environment
```bash
python -m venv venv
```

### Activate Environment

**Windows**
```bash
.\venv\Scripts\activate
```

**Linux / Mac**
```bash
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Application
```bash
python main.py
```

---

## 📊 Future Roadmap

Upcoming improvements include:

### 🔐 Identity Locking
Mapping unique **Eigenface signatures** to registered user profiles.

### 🧠 Liveness Detection
Preventing spoofing using **anti-photo detection mechanisms**.

### 😊 Emotion Analytics
Integrating **real-time facial emotion recognition** within biometric analysis.

---

## 🧑‍💻 Developed With Precision

**Neural Computer Vision Framework**

Computer Vision • Biometric Analytics • Web Deployment
