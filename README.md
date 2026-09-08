# Student Performance Predictor

## Overview

This machine learning project predicts whether a student is likely to **Pass** or **Fail** based on academic and participation-related features.

The project demonstrates a complete machine learning workflow including:

* Data preprocessing
* Label encoding
* Feature scaling
* Model training
* Model evaluation
* Feature importance analysis
* Comparison of multiple machine learning algorithms

---

## Dataset Features

| Feature        | Description                                  |
| -------------- | -------------------------------------------- |
| StudentID      | Unique identifier for each student           |
| Gender         | Male or Female                               |
| StudyHours     | Number of study hours                        |
| PreviousScores | Previous academic scores                     |
| Participation  | Low, Medium, or High classroom participation |
| Performance    | Target variable (Pass/Fail)                  |

---

## Machine Learning Models Used

### 1. Random Forest Classifier

* Ensemble learning algorithm
* Provides feature importance scores
* Handles nonlinear relationships effectively

### 2. K-Nearest Neighbors (KNN)

* Instance-based learning algorithm
* Classifies students based on similar examples

### 3. Support Vector Machine (SVM)

* Powerful classification algorithm
* Effective for separating classes in higher-dimensional spaces

---
##Accuracy 
<img width="702" height="397" alt="Screenshot 2026-06-24 124501" src="https://github.com/user-attachments/assets/580954ec-7ccb-40dd-8809-cb1626ce9c86" />



## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn

---

## Project Workflow

1. Load dataset
2. Encode categorical features
3. Split data into training and testing sets
4. Standardize numerical features
5. Train machine learning models
6. Evaluate model accuracy
7. Generate classification reports
8. Visualize feature importance
9. Compare model performances

---

## Installation

Install the required packages:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

---

## Run the Project

```bash
python student_progress.py
```

---

## Output

The program provides:

* Model Accuracy
* Classification Report
* Random Forest Feature Importance Graph
* Accuracy Comparison Between Models

---

## Future Improvements

* Add cross-validation
* Use larger real-world datasets
* Hyperparameter tuning
* Deploy using Streamlit
* Add confusion matrix visualization
* Compare additional ML models

---

## Author

**Ritik Kumar**

B.Tech Student | Machine Learning Enthusiast | Aspiring AI Engineer

