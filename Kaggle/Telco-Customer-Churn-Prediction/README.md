📊 Telco Customer Churn Prediction using Machine Learning

📌 Project Overview

Customer churn is one of the biggest challenges for subscription-based businesses. Retaining existing customers is often more cost-effective than acquiring new ones.

In this project, I built an end-to-end machine learning pipeline to predict customer churn using the IBM Telco Customer Churn dataset. The project covers data preprocessing, exploratory data analysis (EDA), feature engineering, model development, evaluation, threshold optimization, and business recommendations.

⸻

🎯 Business Problem

The objective is to identify customers who are likely to leave the company (Churn) and help the business take proactive retention actions.

⸻

📂 Dataset

* Dataset: IBM Telco Customer Churn
* Number of customers: 7,043
* Target variable: Churn (Yes / No)

⸻

🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn

⸻

🔍 Exploratory Data Analysis (EDA)

The analysis showed that customer churn is strongly associated with:

* Month-to-month contracts
* Fiber optic internet service
* Electronic check payment method
* Customers without Online Security
* Customers without Tech Support
* Customers with shorter tenure

⸻

🤖 Machine Learning Models

The following models were trained and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest

⸻

📈 Model Performance

Model	ROC-AUC
Logistic Regression	0.842
Random Forest	0.842
Decision Tree	0.830

The final selected model was Logistic Regression because it achieved the best overall performance while remaining highly interpretable.

⸻

⚙️ Threshold Optimization

Instead of using the default threshold (0.50), the classification threshold was optimized to 0.28 to improve customer churn detection.

Final performance:

* Accuracy: 74.88%
* Precision: 51.77%
* Recall: 78.07%
* F1 Score: 62.26%
* ROC-AUC: 84.19%

⸻

💡 Business Insights

The highest-risk customer segment was identified as:

* Month-to-month contract
* Fiber optic internet
* Electronic check payment
* Tenure ≤ 12 months

This segment showed a churn rate of approximately 71%, making it the highest priority for customer retention campaigns.

⸻

📋 Business Recommendations

* Focus retention efforts on new customers during their first year.
* Encourage customers to switch from month-to-month contracts to longer-term plans.
* Offer personalized retention campaigns for high-risk customers.
* Promote Online Security and Tech Support services.
* Deploy the model as an early warning system for customer churn.

⸻

📁 Repository Structure

Telco-Customer-Churn-Prediction/
│
├── Telco Customer Churn Prediction.ipynb
└── README.md

⸻

👤 Author

Saba Nikara

Aspiring Data Scientist | Machine Learning | Data Analytics
