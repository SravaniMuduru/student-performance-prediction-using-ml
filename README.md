🎓 Student Performance Prediction using Machine Learning
📌 Project Overview

This project focuses on predicting student academic performance based on factors such as study time, previous grades, and absences using Machine Learning techniques. The goal is to analyze student data and build a regression model that can accurately predict a student’s final grade.

🧠 Problem Statement

Educational institutions often struggle to identify students who may need academic support at an early stage. By analyzing historical student data, this system predicts student performance and helps enable timely academic intervention.

⚙️ Technologies Used

Programming Language: Python

Libraries:

NumPy

Pandas

Matplotlib

Scikit-learn

Algorithm: Linear Regression

IDE: VS Code

Platform: GitHub

📂 Dataset

Student Performance Dataset

Total Records: 395

Total Features: 33

🔑 Selected Features

Study Time

Absences

First Period Grade (G1)

Second Period Grade (G2)

🎯 Target Variable

Final Grade (G3)

🔄 Project Workflow

Data loading and exploration

Data preprocessing

Feature selection

Train–test split

Model training

Model evaluation

Performance analysis

📊 Model Evaluation

The model was evaluated using standard regression metrics:

Mean Squared Error (MSE): 4.17

R² Score: 0.79

These results indicate that the model performs well in predicting student academic performance.

## 📸 Project Output Screenshots

### 🔹 Model Training Output
![Model Training Output](images/output1.png)

### 🔹 Model Evaluation Metrics
![Model Evaluation](images/output2.png)

### 🔹 Final Prediction Result
![Final Prediction](images/output3.png)

▶️ How to Run the Project

1.Clone the repository
git clone https://github.com/your-username/Student-Performance-Prediction-AIML.git
2.Navigate to the project folder
cd Student-Performance-Prediction-AIML
3.Install dependencies
pip install -r requirements.txt
4.Run the training script
python train.py
python train.py

📈 Future Enhancements

Implement advanced models (Random Forest, XGBoost)

Add detailed data visualization graphs

Build a web interface using Flask or Streamlit

Include additional student behavioral features
