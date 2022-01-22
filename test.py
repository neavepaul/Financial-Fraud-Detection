import pickle
import pandas as pd
loaded_model = pickle.load(open('XGBfraudModelv1.pkl', 'rb'))

txn = input("Txn ID: ")
fraud_no_fraud = ""
csv = pd.read_csv('C:/Users/neave/Documents/unscript/data/AIML Dataset.csv')

row = csv[csv['nameOrig']== txn]

#to get only value 
amount = (row['amount']).to_string(index = False)
step = (row['step']).to_string(index = False)
nameOrig = (row['nameOrig']).to_string(index = False)
oldbalanceOrg = (row['oldbalanceOrg']).to_string(index = False)
newbalanceOrig = (row['newbalanceOrig']).to_string(index = False)
oldbalanceDest = (row['oldbalanceDest']).to_string(index = False)
newbalanceDest = (row['newbalanceDest']).to_string(index = False)
nameDest = (row['nameDest']).to_string(index = False)
amount = (row['amount']).to_string(index = False)
#print
print(amount, step, nameOrig, nameDest, oldbalanceOrg, oldbalanceDest, newbalanceOrig, newbalanceDest)


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