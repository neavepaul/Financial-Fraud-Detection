import pickle
import pandas as pd
loaded_model = pickle.load(open('XGBfraudModelv1.pkl', 'rb'))

txn = input("Txn ID: ")
fraud_no_fraud = ""
csv = pd.read_csv('AIML Dataset.csv')

row = csv[csv['nameOrig']== txn]
row = row.drop(['nameDest','nameOrig','isFraud'], axis = 1)
row['errorBalanceOrig'] = row.newbalanceOrig + row.amount - row.oldbalanceOrg
row['errorBalanceDest'] = row.oldbalanceDest + row.amount - row.newbalanceDest
row['type'].replace('TRANSFER', 0, inplace = True)
row['type'].replace('CASH_OUT', 1, inplace = True)
row['type'].replace('CASH_IN', 2, inplace = True)
row['type'].replace('PAYMENT', 3, inplace = True)
row['type'].replace('DEBIT', 4, inplace = True)



prediction = loaded_model.predict(row)
if prediction == [0]:
    fraud_no_fraud = "FRAUD!!"
else:
    fraud_no_fraud = "Not a Fraud."

print(fraud_no_fraud)
