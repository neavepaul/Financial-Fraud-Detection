from email import header
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

csv = pd.read_csv('AIML Dataset.csv')
app=Flask(__name__)
model = pickle.load(open('XGBfraudModelv1.pkl', 'rb'))

# csv=pd.DataFrame(data_csv)
fraud_no_fraud = ""
# data = pd.read_csv("AIML.csv")

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    txn = request.form.get("id")
    row = csv[csv['nameOrig']== txn]
    
    #obal=str(row.oldbalanceOrg)
    #nbal=str(row.newbalanceOrig)
    #amt=str(row.amount)
    #nd=str(row.nameDest)

    obal= (row['oldbalanceOrg']).to_string(index = False)
    nbal= (row['newbalanceOrig']).to_string(index = False)
    amt = (row['amount']).to_string(index = False)
    nd  = (row['nameDest']).to_string(index = False)
    # display=row.drop(['isFraud','step','isFlaggedFraud','type','nameOrig','oldbalanceDest','newbalanceDest'],axis=1)
    # oldBal=display.oldbalanceOrg
    # print(oldBal)
    row = row.drop(['nameDest','nameOrig','isFraud'], axis = 1)
    row['errorBalanceOrig'] = row.newbalanceOrig + row.amount - row.oldbalanceOrg
    row['errorBalanceDest'] = row.oldbalanceDest + row.amount - row.newbalanceDest
    row['type'].replace('TRANSFER', 0, inplace = True)
    row['type'].replace('CASH_OUT', 1, inplace = True)
    row['type'].replace('CASH_IN', 2, inplace = True)
    row['type'].replace('PAYMENT', 3, inplace = True)
    row['type'].replace('DEBIT', 4, inplace = True)
   
    prediction = model.predict(row)
    if prediction == [0]:
        fraud_no_fraud = "The Transaction is FRAUD!! Call 100 and inform the Bank regarding the same."
    else:
        fraud_no_fraud = "The Transaction is NOT FRAUD!!"
    
    print(fraud_no_fraud)
    return render_template("Home.html", isfraud="{}".format(fraud_no_fraud), oldbal="{}".format(obal), newbal="{}".format(nbal),namedest="{}".format(nd), amt="{}".format(amt))
   
    
if __name__ == '__main__':
    app.run(debug=True)