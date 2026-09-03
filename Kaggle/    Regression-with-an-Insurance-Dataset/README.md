Regression with an Insurance Dataset

📌 Project Overview

This project is a machine learning regression project based on the Kaggle Playground Series S4E12 – Regression with an Insurance Dataset competition.

The main objective is to predict the Premium Amount for insurance customers using demographic, financial, health, policy, and lifestyle-related features.

The project covers the complete machine learning workflow, from data exploration and preprocessing to model training, evaluation, and final prediction generation.

🎯 Objective

The target variable is:

Premium Amount

The competition evaluation metric is Root Mean Squared Logarithmic Error (RMSLE).

📊 Dataset

The dataset contains information about insurance customers, including:

* Age
* Gender
* Annual Income
* Marital Status
* Number of Dependents
* Education Level
* Occupation
* Health Score
* Location
* Policy Type
* Previous Claims
* Vehicle Age
* Credit Score
* Insurance Duration
* Customer Feedback
* Smoking Status
* Exercise Frequency
* Property Type
* Policy Start Date

The dataset is provided by Kaggle as part of the Playground Series S4E12 competition.

🔗 Kaggle Competition:
https://www.kaggle.com/competitions/playground-series-s4e12

🔍 Project Workflow

The following steps were performed:

1. Data loading and inspection
2. Exploratory Data Analysis (EDA)
3. Missing-value analysis
4. Numerical and categorical feature analysis
5. Date feature engineering
6. Data preprocessing
7. Train-validation split
8. Categorical feature encoding
9. Target transformation using log1p
10. Machine learning model development
11. Model comparison using RMSLE
12. Final model training
13. Test-set prediction
14. Submission file generation

🤖 Models

Several regression approaches were evaluated:

* HistGradientBoostingRegressor
* CatBoostRegressor
* LightGBM Regressor

The models were evaluated using RMSLE on the validation set.

Validation Results

Model	Validation RMSLE
HistGradientBoostingRegressor	1.04686
CatBoostRegressor	1.04951
LightGBM Regressor	1.04649

Based on the validation results, LightGBM achieved the best performance among the evaluated models.

🏆 Final Model

The final model was trained using the complete training dataset and used to generate predictions for the test dataset.

The final submission contains:

* 800,000 predictions
* id
* Premium Amount

The generated file is:

submission.csv

📓 Kaggle Notebook

The complete project, including the analysis, preprocessing, model training, evaluation, and predictions, is available in the Kaggle Notebook:

🔗 View Kaggle Notebook

🛠️ Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* CatBoost
* LightGBM
* Matplotlib
* Kaggle

📁 Repository Contents

Regression-with-an-Insurance-Dataset/
│
├── README.md
├── regression-with-an-insurance-dataset.ipynb
└── submission.csv

📈 Key Takeaways

The analysis showed that financial and health-related variables, particularly Annual Income, Credit Score, Health Score, and Previous Claims, were among the most influential features for predicting insurance premiums.

This project demonstrates an end-to-end machine learning workflow for a large-scale regression problem, including preprocessing, feature engineering, model comparison, and final prediction generation.
