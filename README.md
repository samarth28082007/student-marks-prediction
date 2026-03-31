# 🎓 Machine Learning Based Student Score Prediction

## 📌 Project Description

The objective of the project is to create a web application that uses machine learning to predict the scores students will receive based on how many hours they studied. Using Linear Regression concepts, we were able to create an equation representing the relationship between the number of hours studied and the overall score received on an exam.

The complete machine learning process is used to create this application, which consists of the following steps:

1) Collect the Data
2) Train the Model
3) Save the Model
4) Create a Web Application to use the Model

---

## 🚀 Project Features:

* 📊 Predict the score students will receive based on the number of hours spent studying
* ⚡ Fast & Lightweight Machine Learning Model
* 🌐 Interactive Web Application using Streamlit (enters data in real-time)
* 💾 Uses Pickle for saving the machine learning model on the disk
* 🧠 Beginner Friendly, allowing you to easily understand how the model operates as well as the concepts behind it

---

## 🛠️ Project Technology Stack:

* Python
* pandas
* numpy
* scikit-learn
* Streamlit

---

## 📂 Project Structure:

```
PredictStudentScore/
│
├── data/
│   └── student_data.csv    # Data Set
│
├── model/
│   └── model.pkl            # Trained Machine Learning Model
│
├── train.py                 # Model Training Script
├── app.py                   # Streamlit Web Application File
├── requirements.txt         # Requirements
├── README.md                # Setup Instructions for this Project
└── .gitignore               # Ignored Files
```

---

## 📊 Dataset Description:

The dataset used for this project contains two pieces of information:

* Input = Number of Hours Students Studied
* Output = Marks Out of Maximum Possible Marks Received by a Student

The dataset is used as a primary example of the way a machine learning model would be applied to producing applications in the real world.


## 🤖 Model Used

The model used in this project is:

### 🔹 Linear Regression

Linear Regression is a supervised machine learning algorithm used to predict a continuous value.

It works on the equation:

y = mx + c

Where:

* y = Predicted marks
* x = Study hours
* m = Slope (coefficient)
* c = Intercept

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/samarth28082007/student-marks-prediction.git
cd student-marks-prediction
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Train the model

```
python train.py
```

---

### 4️⃣ Run the application

```
streamlit run app.py
```

---

## 🌐 Usage

1. Open the app in your browser
2. Enter the number of study hours
3. Click on **Predict**
4. View the predicted marks instantly

---

## 📸 Output Screenshot

<img width="1747" height="713" alt="Screenshot 2026-03-30 172039" src="https://github.com/user-attachments/assets/9c46ba9f-d80c-489c-a3c3-70084794d072" />

<img width="1783" height="694" alt="Screenshot 2026-03-30 172111" src="https://github.com/user-attachments/assets/4b5436bc-b422-43ee-a8a2-aaf7bfdcd522" />

---

## 📈 Example Prediction

| Study Hours | Predicted Marks |
| ----------- | --------------- |
| 2           | ~25             |
| 5           | ~47             |
| 8           | ~75             |

---

## ⚠️ Limitations

* Uses only one feature (study hours)
* Does not consider real-life factors like:

  * Attendance
  * Sleep
  * Study quality

---

## 🔮 Future Improvements

* Add multiple input features
* Improve UI design
* Deploy the app online
* Add graphs and visualization
* Use advanced ML models

---

## 👨‍💻 Author

**Samarth Gupta**

---

## 📄 License

This project is open-source and available for educational purposes.

---

## ⭐ Acknowledgements

* Scikit-learn documentation
* Streamlit documentation
* Open-source ML community


