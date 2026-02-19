<<<<<<< HEAD
# 🔬 Hematovision: Advanced Blood Cell Classification

An intelligent web-based application for automatic blood cell classification using Transfer Learning and MobileNetV2 deep learning model.

**Project Title:** Hematovision - An Advanced Blood cells classification using Transfer Learning  
**Team ID:** LTVIP2026TMIDS65885  
**Program:** SmartBridge Long Internship

---

## 👥 Team Members

| Role            | Name                          |
| --------------- | ----------------------------- |
| **Team Leader** | Rayapudi Anil Kumar           |
| **Team Member** | Rebba Gopi                    |
| **Team Member** | Sakhamuri Bharath Chandra Sai |
| **Team Member** | Sane Sasikala                 |

---

## 📋 Project Overview

Hematovision is a Flask-based web application that leverages transfer learning with MobileNetV2 to classify blood cell images into three categories:

- **RBC** (Red Blood Cells)
- **WBC** (White Blood Cells)
- **Platelet** (Platelets)

The application provides a user-friendly interface for uploading microscopic blood cell images and receiving instant classification results with confidence scores.

---

## ✨ Features

- 🎯 **Accurate Classification** - Uses pre-trained MobileNetV2 model with transfer learning
- 🖼️ **Web-based Interface** - Easy-to-use Flask web application
- 📱 **Responsive Design** - Works on desktop and mobile devices
- 🎨 **Modern UI** - Professional medical color scheme (teal & emerald)
- ⚡ **Fast Processing** - Lightweight MobileNetV2 model for quick inference
- 📊 **Confidence Scores** - Shows prediction confidence for each classification

---

## 🛠️ Tech Stack

- **Backend:** Python 3.12 with Flask
- **Deep Learning:** TensorFlow/Keras with MobileNetV2
- **Frontend:** HTML5, CSS3, JavaScript
- **Database:** Optional (for production)
- **Deployment:** Can be deployed on AWS, Heroku, or local servers

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- pip package manager

### Setup Instructions

1. **Clone the repository**

   ```bash
   git clone <repository_url>
   cd Hematovision-main/Project
   ```

2. **Create a virtual environment** (optional but recommended)

   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**

   ```bash
   pip install -r templates/requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Access the web interface**
   - Open your browser and navigate to: `http://localhost:5000`

---

## 🚀 Usage

1. **Upload Image**
   - Click on the upload area or select a file
   - Choose a blood cell microscopy image (JPG, JPEG, or PNG)

2. **Get Classification**
   - Click "Classify Blood Cell"
   - The model will process and classify the image

3. **View Results**
   - See the predicted cell type
   - View confidence percentage
   - Learn more about the classified cell type

---

## 📁 Project Structure

```
Hematovision-main/
├── Project/
│   ├── app.py                          # Flask application
│   ├── create_model.py                 # Model creation script
│   ├── generate_demo_images.py         # Demo image generator
│   ├── requirements.txt                # Python dependencies
│   ├── static/
│   │   ├── style.css                   # UI styling
│   │   └── images/                     # Generated images directory
│   │       ├── demo_rbc.png
│   │       ├── demo_wbc.png
│   │       ├── demo_platelet.png
│   │       └── demo_mixed.png
│   ├── templates/
│   │   ├── blood_cell_classifier_mobilenetv2 (1).h5  # Pre-trained model
│   │   ├── home.html                   # Home page
│   │   ├── result.html                 # Results page
│   │   └── requirements.txt
│   └── Dataset/                        # Training data (if available)
└── README.md

```

---

## 🧠 Model Details

- **Model Type:** Convolutional Neural Network (CNN)
- **Base Architecture:** MobileNetV2 (pre-trained on ImageNet)
- **Transfer Learning:** Fine-tuned on blood cell classification task
- **Input Size:** 224 x 224 pixels
- **Output Classes:** 3 (RBC, WBC, Platelet)
- **Train/Test Split:** Standard TRAIN/TEST directory structure

---

## 📊 Testing with Demo Images

1. Run the demo image generator:

   ```bash
   python generate_demo_images.py
   ```

2. Access demo images from `static/images/` folder:
   - `demo_rbc.png` - Sample Red Blood Cell
   - `demo_wbc.png` - Sample White Blood Cell
   - `demo_platelet.png` - Sample Platelet
   - `demo_mixed.png` - Mixed cell sample

3. Upload any demo image through the web interface to test

---

## 🎨 Color Scheme

- **Primary Teal:** `#0891b2` - Modern, trustworthy
- **Dark Teal:** `#0e7490` - Hover states
- **Emerald Green:** `#10b981` - Positive outcomes (confidence)
- **Background:** Light blue-gray for medical theme

---

## 🔄 Workflow

```
User Upload Image
    ↓
Flask receives file
    ↓
Image preprocessed (224x224, normalized)
    ↓
MobileNetV2 model inference
    ↓
Classification output (3 classes)
    ↓
Display results with confidence
```

---

## 🚀 Future Enhancements

- [ ] Add more cell types (Neutrophils, Eosinophils, Monocytes, Lymphocytes)
- [ ] Implement batch processing for multiple images
- [ ] Add data visualization and statistics
- [ ] Create REST API for integration with other systems
- [ ] Deploy on cloud platform (AWS, Google Cloud)
- [ ] Add model retraining pipeline
- [ ] Implement confidence threshold alerts
- [ ] Add historical data tracking for users

---

## 📝 Requirements

See [requirements.txt](templates/requirements.txt) for all dependencies including:

- TensorFlow/Keras
- Flask
- OpenCV
- NumPy
- Scikit-learn
- And more...

---

## ⚠️ Disclaimer

This application is designed for educational and research purposes. For clinical use, proper validation and regulatory approval are required. Always consult medical professionals for diagnosis.

---

## 📧 Contact & Support

For questions or support, please reach out to the team members listed above.

---

## 📄 License

This project is developed as part of the SmartBridge Long Internship Program 2025.

---

**Last Updated:** February 17, 2026  
**Status:** Active Development ✅
=======
# Hematovision
>>>>>>> 11e00a2f9fbdaef28de440d606b13b58846a1929
