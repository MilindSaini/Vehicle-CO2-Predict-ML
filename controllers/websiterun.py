from app import app
from flask import render_template,request
import numpy as np
import pickle


model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
    d1=request.form.get('a')
    d2=request.form.get('b')
    d3=request.form.get('c')
    d4=request.form.get('d')
    d5=request.form.get('e')
    d6=request.form.get('f')
    arr=np.array([[d1,d2,d3,d4,d5,d6]])
    pred=model.predict(arr)
    output=(pred[0])
    return render_template('home.html',prediction_text="Carbon Emissions : %1f mg/km" %(output))



if __name__ == '__main__':
    app.run(debug=True)

