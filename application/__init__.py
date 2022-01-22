from flask import Flask, render_template, request
import pickle
import numpy as np

app=Flask(__name__)
model = pickle.load(open('XGBfraudModelv1.pkl','rb'))

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/predict', methods=['POST'])
def predict():
    nameOrig_val= request.form.values()
    
if __name__ == '__main__':
    app.run(debug=True)