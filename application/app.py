from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app=Flask(__name__)
model = pickle.load(open('XGBfraudModelv1.pkl', 'rb'))
data_csv = pd.read_csv('static/AIML.csv', header=0)
csv=pd.DataFrame(data_csv)
fraud_no_fraud = ""
# data = pd.read_csv("AIML.csv")

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    txn= request.form.values()
    print(txn)
    # fraud_no_fraud = ""
    row = csv[csv['nameOrig']== txn]
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
        fraud_no_fraud = "FRAUD!!"
    else:
        fraud_no_fraud = "Not a FRAUD!!"
    
    print(fraud_no_fraud)
    return render_template("Home.html", pred="GOT VALUESSSS {}".format(fraud_no_fraud))
    
if __name__ == '__main__':
    app.run(debug=True)