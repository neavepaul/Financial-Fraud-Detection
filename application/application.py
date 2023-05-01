from flask import Flask, render_template, request
import pandas as pd
import xgboost as xgb

csv = pd.read_csv('data.csv')
application=Flask(__name__)
model = xgb.Booster()
model.load_model('model.bin')

fraud_no_fraud = ""

@application.route('/')
def home():
    return render_template('Home.html')

@application.route('/predict',methods=['POST','GET'])
def predict():
    txn = request.form.get("id")
    row = csv[csv['nameOrig']== txn]


    obal= (row['oldbalanceOrg']).to_string(index = False)
    nbal= (row['newbalanceOrig']).to_string(index = False)
    amt = (row['amount']).to_string(index = False)
    nd  = (row['nameDest']).to_string(index = False)

    row = row.drop(['nameDest','nameOrig','isFraud'], axis = 1)
    row['errorBalanceOrig'] = row.newbalanceOrig + row.amount - row.oldbalanceOrg
    row['errorBalanceDest'] = row.oldbalanceDest + row.amount - row.newbalanceDest
    row['type'].replace('TRANSFER', 0, inplace = True)
    row['type'].replace('CASH_OUT', 1, inplace = True)
    row['type'].replace('CASH_IN', 2, inplace = True)
    row['type'].replace('PAYMENT', 3, inplace = True)
    row['type'].replace('DEBIT', 4, inplace = True)

    row = xgb.DMatrix(row)
    prediction = int(model.predict(row))
    if prediction == 0:
        fraud_no_fraud = "The Transaction is FRAUD!!"
    else:
        fraud_no_fraud = "The Transaction is NOT FRAUD!!"
    
    print(fraud_no_fraud)
    return render_template("Home.html", isfraud="{}".format(fraud_no_fraud), oldbal="{}".format(obal), newbal="{}".format(nbal),namedest="{}".format(nd), amt="{}".format(amt))
   
    
if __name__ == '__main__':
    application.run(debug=True)