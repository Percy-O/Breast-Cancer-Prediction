
# 🧬 Breast Cancer Prediction System (CNN + Django)

A full-stack AI-powered web application for breast cancer detection using Convolutional Neural Networks (CNNs) and the MXNet deep learning framework. This solution empowers healthcare providers to upload mammogram images and receive **real-time predictions** (Positive/Negative) via a clean, user-friendly Django interface.

---

## 📌 Project Overview

Breast cancer early detection is crucial for patient survival. This project bridges **AI and healthcare** by combining a powerful deep learning model with a robust web platform. Users can register/login, upload images, and instantly get predictions on whether the image indicates the presence of breast cancer.

---

## ⚙️ Technologies Used

### 🔢 Backend & Machine Learning

* **Python 3.8+**
* **MXNet (Gluon API)** – CNN for image classification
* **Scikit-learn** – model evaluation
* **NumPy, Pandas** – data processing

### 🌐 Web Development

* **Django** – backend web framework
* **Django Authentication** – user login/register system
* **HTML, CSS, Bootstrap** – front-end design
* **Pillow** – image processing
* **OpenCV** – image reading and resizing

### 🧠 Model Architecture

* CNN with two convolutional layers, max pooling, dense layers, dropout
* Image resized to **50x50** and normalized
* Trained on labeled mammogram images (positive/negative)

---

## 🗂 Project Structure

```
breast_cancer_webapp/
│
├── breast_model.params               # Trained CNN model weights (MXNet)
├── media/uploads/                    # User-uploaded mammogram images
├── static/                           # Static files (CSS, JS, images)
├── templates/                        # HTML templates
│   ├── index.html                    # Home page
│   ├── login.html                    # Login form
│   ├── register.html                 # Registration form
│   └── result.html                   # Prediction results page
├── core/
│   ├── views.py                      # Image upload logic + model loading
│   ├── models.py                     # Django model for uploads
│   ├── forms.py                      # Image upload form
│   ├── urls.py                       # App-level routing
│   └── utils.py                      # Preprocessing & prediction logic
├── manage.py                         # Django entry point
├── db.sqlite3                        # Default SQLite database
└── README.md                         # Project documentation
```

---

## 🖼️ Sample Workflow

1. User registers or logs in.
2. Uploads a breast image (PNG/JPG).
3. Image is resized and normalized.
4. Pre-trained CNN model (`.params`) is loaded.
5. Prediction is displayed: **Cancer Detected / No Cancer Detected**

---

## 🚀 Getting Started

### 🔧 Setup Instructions

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/breast-cancer-detection-django.git
   cd breast-cancer-detection-django
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```bash
   python manage.py migrate
   ```

5. **Run the server**

   ```bash
   python manage.py runserver
   ```

6. **Visit in your browser**

   ```
   http://127.0.0.1:8000/
   ```

---

## ✅ Features

* 🔐 User Authentication (Register, Login, Logout)
* 🧠 Real-time CNN Model Prediction
* 📂 Secure Image Upload Handling
* 📊 Result Display (Prediction + Confidence)
* 🎨 Clean UI using Bootstrap

---

## 📈 Model Evaluation

* Achieved **high accuracy** on unseen test data
* Metrics:

  * **Accuracy**
  * **F1 Score**
  * **Precision**
  * **Recall**
* Visualized via:

  * Confusion Matrix
  * ROC Curve

---

## 📬 Contact

**Author:** Percy Owoeye
**GitHub:** [@yourusername](https://github.com/yourusername)
**Email:** [your.email@example.com](mailto:your.email@example.com)

---

## 🙌 Acknowledgement

Special thanks to the open-source community and MXNet for enabling scalable deep learning workflows, and Django for a seamless backend experience.

---

## 🏥 Disclaimer

This system is **for educational and experimental purposes only** and should **not be used for actual clinical diagnosis** without expert validation.
