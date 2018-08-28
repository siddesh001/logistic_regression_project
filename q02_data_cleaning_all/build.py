# %load q02_data_cleaning_all/build.py
# Default Imports
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname('__file__'))))
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.logistic_regression_project.q01_outlier_removal.build import outlier_removal

loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
loan_data = loan_data.drop('Loan_ID', 1)
loan_data = outlier_removal(loan_data)


# Write your solution here :
def data_cleaning(data):
    numeric=['LoanAmount']
    
    categorical=['Gender', 'Married', 'Dependents', 'Self_Employed', 'Loan_Amount_Term', 'Credit_History']
    
    
    for n in numeric:
        loan_data[n].fillna(data[n].mean(),inplace=True)
    
    for c in categorical:
        loan_data[c].fillna(data[c].mode(),inplace=True)
    
    X=loan_data.drop('Loan_Status',axis=1)
    y=loan_data['Loan_Status']
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=.25,random_state=9)
    
    return X,y, X_train,X_test,y_train,y_test


