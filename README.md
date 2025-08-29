# 📊 Customer Churn Prediction

This project predicts whether a customer is likely to **churn (leave)** or **stay**, using machine learning models.  
Churn prediction helps businesses identify at-risk customers and take proactive actions to improve retention.  

---

## 🚀 Project Overview
- **Goal:** Predict customer churn (Yes/No) based on customer attributes.  
- **Dataset:** Customer data containing demographics, account information, and service usage.  
- **Techniques:** Data preprocessing, feature encoding, scaling, hyperparameter tuning, and model evaluation.  
- **Models Used:**
  - Logistic Regression  
  - K-Nearest Neighbors (KNN)  
  - Support Vector Machine (SVM)  
  - Decision Tree  
  - Random Forest  

---

## ⚙️ Workflow
1. **Data Preprocessing**
   - Handle missing values  
   - Encode categorical variables (Label Encoding / One-Hot Encoding)  
   - Scale features for distance-based models (KNN, SVM)  

2. **Model Building**
   - Train multiple ML models  
   - Hyperparameter tuning using **GridSearchCV**  

3. **Evaluation**
   - Accuracy, Precision, Recall, F1-score  
   - Confusion Matrix & Classification Report  

---

## 📈 Results
- Best Model: **Random Forest (with hyperparameter tuning)**  
- Achieved Accuracy: **XX%** (replace with your actual result)  
- Key Insights:  
  - Customers with shorter tenure are more likely to churn  
  - Month-to-month contracts have higher churn rates  
  - Electronic check payments are common among churned customers  

---

## 🛠️ Tech Stack
- **Language:** Python 🐍  
- **Libraries:** pandas, numpy, matplotlib, seaborn, scikit-learn  
- **Tools:** Jupyter Notebook / VS Code  

---

## 📂 Project Structure
Customer-Churn-Prediction/
|-- venv
│-- dataset
│-- notebook filre
│-- app.py # training script
│-- requirements.txt # dependencies
│-- README.md # documentation