Multi-Disease Prediction System

📌 Project Overview

The Multi-Disease Prediction System is a machine learning–based web application that predicts the likelihood of multiple diseases using both structured medical data and skin image classification.
The system helps in early detection, supports quick medical insights, and demonstrates the integration of machine learning with a web interface.

---

🚀 Features

- Predicts diseases using symptom-based structured data
- Skin disease detection using deep learning image classification
- Supports multiple disease types in a single unified platform
- Real-time prediction through an interactive web interface
- Clean UI built with HTML, CSS, and Flask templates

---

🛠️ Tech Stack

Frontend: HTML, CSS
Backend: Python, Flask
Machine Learning:

- Random Forest for structured medical datasets
- MobileNetV2 CNN for skin disease image classification

Other Tools: NumPy, Pandas, Scikit-learn, TensorFlow/Keras

---

📂 Project Structure

Multi-Disease-Prediction/
│
├── models/              # Trained ML/DL models
├── static/              # CSS, images, and frontend assets
├── templates/           # HTML templates for UI
├── app.py               # Main Flask application
├── Train.py             # Model training script
├── heart.csv            # Heart disease dataset
├── kidney_disease.csv   # Kidney disease dataset
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation

---

⚙️ Installation & Setup

1️⃣ Clone the repository

git clone https://github.com/your-username/Multi-Disease-Prediction.git
cd Multi-Disease-Prediction

2️⃣ Create virtual environment (optional but recommended)

python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run the application

python app.py

5️⃣ Open in browser

http://127.0.0.1:5000

---

📊 Machine Learning Workflow

- Data preprocessing and cleaning
- Feature selection and normalization
- Model training using Random Forest and CNN
- Model evaluation with accuracy and performance metrics
- Integration into a real-time Flask web application

---

🎯 Future Enhancements

- Add more disease prediction modules
- Improve model accuracy with larger datasets
- Deploy the system on cloud platforms
- Add user authentication and medical report history

---

👩‍💻 Author

Chavadi Kiran Ganesh 
Computer Science Engineering Student
Passionate about Software Development, Machine Learning, and Full-Stack Applications

---

📜 License

This project is for educational and research purposes only and not intended for real medical diagnosis.
