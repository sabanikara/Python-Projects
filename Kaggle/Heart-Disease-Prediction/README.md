# Heart Disease Prediction using Machine Learning

This project aims to predict the presence of heart disease using machine learning classification algorithms.

The dataset contains medical attributes such as age, cholesterol level, maximum heart rate, chest pain type, and other clinical features.

Several machine learning models were developed and compared, including Logistic Regression, Decision Tree, and Random Forest.

## Dataset

The dataset contains 1025 records and 13 medical features.

Features include:
- Age
- Sex
- Chest pain type (cp)
- Resting blood pressure
- Cholesterol
- Maximum heart rate (thalach)
- Exercise-induced angina
- Oldpeak
- ST slope
- Thal
- Other clinical attributes

Target:
- 0 → No Heart Disease
- 1 → Heart Disease

Duplicate records were removed during data preprocessing, resulting in 302 unique samples.

## Machine Learning Models

The following classification models were implemented:

- Logistic Regression
- Decision Tree
- Random Forest
- Tuned Random Forest using GridSearchCV


## Model Performance

| Model | Accuracy |
|---|---|
| Logistic Regression | 77% |
| Decision Tree | 74% |
| Random Forest | 84% |
| Tuned Random Forest | 84% |

Random Forest achieved the best performance with an accuracy of approximately 83.6%.


## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
