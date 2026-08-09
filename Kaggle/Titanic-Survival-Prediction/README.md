🔗 Kaggle Notebook

The original Kaggle Notebook for this project is available here:

View the project on Kaggle
Titanic Survival Prediction 🚢

A machine learning project for predicting passenger survival using the Titanic dataset from Kaggle.

📌 Project Overview

This project is an end-to-end machine learning workflow created as a practical project while learning Data Science and Machine Learning.

The goal is to explore the Titanic dataset, clean and prepare the data, create useful features, train classification models, evaluate their performance, and generate predictions for the Kaggle test dataset.

🔎 Exploratory Data Analysis

The analysis included:

* Checking the target variable distribution
* Identifying missing values
* Exploring passenger class and gender
* Analyzing age and fare distributions
* Investigating family size
* Investigating ticket group size
* Exploring cabin availability
* Analyzing embarkation points
* Examining relationships between features and survival

🛠️ Feature Engineering

The following features were created or transformed:

* HasCabin — indicates whether cabin information was available
* Title — extracted from passenger names
* Master, Miss, Mr, Mrs, Rare — one-hot encoded title features
* Embarked_C, Embarked_Q, Embarked_S — one-hot encoded embarkation features
* TicketGroupSize — number of passengers sharing the same ticket
* FamilySize — calculated from SibSp and Parch
* Missing Age values were filled using the training-set median
* Missing Fare values in the test set were filled using the training-set median
* Sex was converted into numerical values

🤖 Machine Learning Models

Two classification models were evaluated:

Logistic Regression

Local test performance:

Metric	Score
Accuracy	0.844
Precision	0.797
Recall	0.797
F1 Score	0.797

Random Forest

The Random Forest model was evaluated and tuned using cross-validation.

Best parameters:

max_depth = 5
min_samples_split = 5
n_estimators = 100

Best Cross-Validation Accuracy:

0.827

Final Test Accuracy:

0.804

📊 Model Comparison

Metric	Logistic Regression	Random Forest
Accuracy	0.844	0.804
Precision	0.797	0.766
Recall	0.797	0.710
F1 Score	0.797	0.737

Based on the local evaluation, Logistic Regression performed better than Random Forest in this version of the project.

🏆 Kaggle Result

The final Logistic Regression model was used to generate predictions for the Kaggle test dataset.

Kaggle Public Score: 0.76794

💡 Key Findings

Feature analysis showed that variables such as Sex, passenger class, age, fare, cabin availability, and passenger title were important in predicting survival.

The project also demonstrated how feature engineering and proper preprocessing can improve the performance of machine learning models on tabular data.

🧰 Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Kaggle

📁 Project Structure

Titanic-Survival-Prediction/
│
├── README.md
└── Titanic_Survival_Prediction.ipynb

🎯 Machine Learning Workflow

Data Loading
     ↓
Data Cleaning
     ↓
Exploratory Data Analysis
     ↓
Feature Engineering
     ↓
Train / Test Split
     ↓
Feature Scaling
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Cross-Validation
     ↓
Hyperparameter Tuning
     ↓
Prediction
     ↓
Kaggle Submission

👩‍💻 Author

Saba Nik Ara

This project is part of my ongoing journey into Data Analysis, Data Science, and Machine Learning.
