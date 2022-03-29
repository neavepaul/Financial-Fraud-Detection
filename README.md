# UnSriptRookies22_Archarios
UnScript Rookie’s Hackathon 2022. An Pan-India hackathon exclusively for 2nd Year Engineering Students

## AIML Problem Statement:
### Financial Management System:
The Financial Management System is a software that is used to check the authenticity of a particular transaction in a financial company.
In Financial Management System, participants must create a model for predicting fraudulent transactions for a financial company and then use the model's insights to create an actionable plan. The case's data is stored in a CSV file with 
6362620 rows and 10 columns.

------------------------------------------------------------------------------------

We imported the data from the csvfile and perform some analysis on it to find certain trends.  
We then used CatBoostClassifier to create a model which we trained.  
We then shifted to XGBoost which is better for numeric values.  
XGBoost applies a better regularization technique to reduce overfitting, and it is one of the differences from the gradient boosting. The xgboost.XGBClassifier is a scikit-learn API compatible class for classification. We created our machine learning model using XGBClassifier.  
We then performed some more manipulation of the data and the passed the fields to the model.  
From our self analysis, we noticed that whenever amount=oldbalanceOrig, isFraud is always equal to 1. This basically means that the transfer or cash_out is trying to empty the Orig account. Out of the 8213 fraud cases in the dataset, this condition helps to identify 8034 fraud cases.
The remaining 179 fraud cases contain 154 Transfer transactions out of which 145 have amount = 1.0E7 and 25 Cash_out cases.

------------------------------------------------------------------------------------

**Solution to Prevent Further Fraudulent Transactions**  
Since most of the fraudulent transactions had happened when the fraudster tried to empty the Orig account. We could add a compulsory minimum deposit which should always be available in the account. Checking accounts where a transfer type transaction leaves the newbalance and oldbalance unchanged. Thus showing that the amount hasn't reached the destination and a fraudulent activity took place. Also scrutinizing the transactions around the end of the month (step: 718<) since many fraudulent activities tend to take place during that particular timeline. Transfer amounts of 1.0E7 are showing a pattern of being potential fraudulent transactions, so we could also flag transfer transactions greater than 1.0E7 and keep a track on them.

------------------------------------------------------------------------------------
  
![image](https://user-images.githubusercontent.com/73381366/150656628-b526bb8c-ba81-428f-bf35-4f659fae8c6e.png)
