from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

application = Flask(__name__)
@application.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@application.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        LIMIT_BAL = int(request.form['LIMIT_BAL'])
        AGE = int(request.form['AGE'])
        EDUCATION = request.form['EDUCATION']
        if(EDUCATION=='Graduate school'):
            EDUCATION_1 = 1
            EDUCATION_2 = 0
            EDUCATION_3 = 0
            EDUCATION_4 = 0
        elif (EDUCATION =='University'):
            EDUCATION_1 =0
            EDUCATION_2 =1
            EDUCATION_3 = 0
            EDUCATION_4 = 0
        elif(EDUCATION=='High school'):
            EDUCATION_1 = 0
            EDUCATION_2 = 0
            EDUCATION_3 = 1
            EDUCATION_4 = 0
        elif(EDUCATION =='other'):
            EDUCATION_1 = 0
            EDUCATION_2 = 0
            EDUCATION_3 = 0
            EDUCATION_4 = 1
        else:
            EDUCATION_1 = 0
            EDUCATION_2 = 0
            EDUCATION_3 = 0
            EDUCATION_4 = 0


        SEX = request.form['SEX']
        if(SEX=='Male'):
            SEX_1 =1
            SEX_2 =0
        elif(SEX=='Female'):
            SEX_1 =0
            SEX_2 =1
        else:
            SEX_1=0
            SEX_2=0

        MARRIAGE = request.form['MARRIAGE']
        if(MARRIAGE=='Married'):
            MARRIAGE_1 =1
            MARRIAGE_2 = 0
            MARRIAGE_3 = 0
        elif (MARRIAGE=='Not married'):
            MARRIAGE_1 = 0
            MARRIAGE_2 = 1
            MARRIAGE_3 = 0
        elif(MARRIAGE =='other'):
            MARRIAGE_1 = 0
            MARRIAGE_2 = 0
            MARRIAGE_3 = 1
        else:
            MARRIAGE_1 = 0
            MARRIAGE_2 = 0
            MARRIAGE_3 = 0

        PAY_0 = request.form['April']
        if(PAY_0 == 'pay duly'):
            PAY_0 = -1
        elif(PAY_0== '1 month delay'):
            PAY_0 = 1
        elif(PAY_0== '2 month delay'):
            PAY_0 = 2
        elif (PAY_0 == '3 month delay'):
            PAY_0 = 3
        elif (PAY_0 == '4 month delay'):
            PAY_0 = 4
        elif (PAY_0 == '5 month delay'):
            PAY_0 = 5
        elif (PAY_0 == '6 month delay'):
            PAY_0 = 6
        elif (PAY_0 == '7 month delay'):
            PAY_0 = 7
        elif (PAY_0 == '8 month delay'):
            PAY_0 = 8
        else:
            PAY_0 = 9



        PAY_2 = request.form['June']
        if (PAY_2 == 'PAY DULY'):
            PAY_2 = -1
        elif (PAY_2 == '1 month delay'):
            PAY_2 = 1
        elif (PAY_2 == '2 month delay'):
            PAY_2 = 2
        elif (PAY_2 == '3 month delay'):
            PAY_2 = 3
        elif (PAY_2 == '4 month delay'):
            PAY_2 = 4
        elif (PAY_2 == '5 month delay'):
            PAY_2 = 5
        elif (PAY_2 == '6 month delay'):
            PAY_2 = 6
        elif (PAY_2 == '7 month delay'):
            PAY_2 = 7
        elif (PAY_2 == '8 month delay'):
            PAY_2 = 8
        else:
            PAY_2 = 9

        PAY_3 = request.form['April']
        if (PAY_3== 'PAY DULY'):
            PAY_3 = -1
        elif (PAY_3 == '1 month delay'):
            PAY_3 = 1
        elif (PAY_3 == '2 month delay'):
            PAY_3 = 2
        elif (PAY_3 == '3 month delay'):
            PAY_3 = 3
        elif (PAY_3 == '4 month delay'):
            PAY_3 = 4
        elif (PAY_3 == '5 month delay'):
            PAY_3 = 5
        elif (PAY_3 == '6 month delay'):
            PAY_3 = 6
        elif (PAY_3 == '7 month delay'):
            PAY_3 = 7
        elif (PAY_3 == '8 month delay'):
            PAY_3 = 8
        else:
            PAY_3 = 9

        PAY_4 = request.form['April']
        if (PAY_4 == 'PAY DULY'):
            PAY_4 = -1
        elif (PAY_4 == '1 month delay'):
            PAY_4 = 1
        elif (PAY_4 == '2 month delay'):
            PAY_4 = 2
        elif (PAY_4 == '3 month delay'):
            PAY_4= 3
        elif (PAY_4 == '4 month delay'):
            PAY_4 = 4
        elif (PAY_4 == '5 month delay'):
            PAY_4 = 5
        elif (PAY_4 == '6 month delay'):
            PAY_4 = 6
        elif (PAY_4 == '7 month delay'):
            PAY_4 = 7
        elif (PAY_4 == '8 month delay'):
            PAY_4 = 8
        else:
            PAY_4 = 9

        PAY_5 = request.form['April']
        if (PAY_5 == 'PAY DULY'):
            PAY_5 = -1
        elif (PAY_5 == '1 month delay'):
            PAY_5 = 1
        elif (PAY_5 == '2 month delay'):
            PAY_5 = 2
        elif (PAY_5 == '3 month delay'):
            PAY_5 = 3
        elif (PAY_5 == '4 month delay'):
            PAY_5 = 4
        elif (PAY_5 == '5 month delay'):
            PAY_5 = 5
        elif (PAY_5 == '6 month delay'):
            PAY_5 = 6
        elif (PAY_5 == '7 month delay'):
            PAY_5 = 7
        elif (PAY_5 == '8 month delay'):
            PAY_5 = 8
        else:
            PAY_5 = 9

        PAY_6 = request.form['May']
        if (PAY_6 == 'PAY DULY'):
            PAY_6 = -1
        elif (PAY_6 == '1 month delay'):
            PAY_6 = 1
        elif (PAY_6 == '2 month delay'):
            PAY_6 = 2
        elif (PAY_6 == '3 month delay'):
            PAY_6 = 3
        elif (PAY_6 == '4 month delay'):
            PAY_6 = 4
        elif (PAY_6 == '5 month delay'):
            PAY_6 = 5
        elif (PAY_6 == '6 month delay'):
            PAY_6 = 6
        elif (PAY_6 == '7 month delay'):
            PAY_6 = 7
        elif (PAY_6 == '8 month delay'):
            PAY_6 = 8
        else:
            PAY_6 = 9

        BILL_AMT1 = float(request.form['BILL_AMT1'])
        BILL_AMT2 = float(request.form['BILL_AMT2'])
        BILL_AMT3 = float(request.form['BILL_AMT3'])
        BILL_AMT4 = float(request.form['BILL_AMT4'])
        BILL_AMT5 = float(request.form['BILL_AMT5'])
        BILL_AMT6 = float(request.form['BILL_AMT6'])

        PAY_AMT1 = float(request.form['PAY_AMT1'])
        PAY_AMT2 = float(request.form['PAY_AMT2'])
        PAY_AMT3 = float(request.form['PAY_AMT3'])
        PAY_AMT4 = float(request.form['PAY_AMT4'])
        PAY_AMT5 = float(request.form['PAY_AMT5'])
        PAY_AMT6 = float(request.form['PAY_AMT6'])

        model = pickle.load(open("rf_model.pkl", "rb"))

        prediction = model.predict([[
            LIMIT_BAL,
               AGE,
               PAY_0,
               PAY_2,
               PAY_3,
               PAY_4,
               PAY_5,
              PAY_6,
              BILL_AMT1,
              BILL_AMT2,
              BILL_AMT3,
              BILL_AMT4,
              BILL_AMT5,
              BILL_AMT6,
              PAY_AMT1,
              PAY_AMT2,
              PAY_AMT3,
              PAY_AMT4,
              PAY_AMT5,
              PAY_AMT6,
            SEX_1,
            SEX_2, MARRIAGE_1, MARRIAGE_2, MARRIAGE_3, EDUCATION_1, EDUCATION_2, EDUCATION_3, EDUCATION_4

        ]])

        if (prediction==1):
            output = 'DEFAULTER'
        else:
            output = "NOT DEFAULTER"
        return render_template('index.html', prediction_text= 'The person is  {}'.format(output))

    return render_template("index.html")

if __name__ == "__main__":
    # application.run(debug=True)
    application.run(host='127.0.0.1', port=5001, debug=True)



















