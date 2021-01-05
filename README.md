# End-to-end-Credit-Card-Defaulter
Credit Card Defaulter Classifier project with Deployment

I used kaggle dataset to build machine learning classifer that classifies a person to a dafaulter or not. Then I deployed this as a web application using Flask framework
### Demo
![image](https://user-images.githubusercontent.com/54037847/103347149-2d584a00-4abc-11eb-9140-b19184a43281.png)
![image](https://user-images.githubusercontent.com/54037847/103347169-3fd28380-4abc-11eb-9478-e174dfc83a2f.png)

You can go and check the application with the link : https://credit-card-defaulter-app.herokuapp.com/

In this project I am going to take a machine learning approch to detect weather a person will be a defaulter or not. A person is said to be a Credit card defaulter if he fails to pay the Minimum Amount Due on the credit card for a few months. this project may help banks to predict if a person will be a defaulter or not so that they may know how much money are they going to collect this month.

This repository was created to help clarify how to utilise flask and gunicorn to easily deploy a python/keras deep learning model as a web app on Heroku. This example features code for online deployment of a classification model , based on scikit-learn models. The trained model achieved accuracy of more than 95% on the test set and its weights have been saved

A JavaScript app running on the browser calls the Flask app (app.py) to load the model weights and return results to the JavaScript app (through the 'GET' and 'POST' methods).
