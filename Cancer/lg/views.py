from django.shortcuts import render
from django.contrib.auth.models import User,auth
# Create your views here.

def home(request):
    return render(request,"home.html")
def input(request):
    return render(request,"input.html")
def output(request):
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import sklearn.datasets
    #loading the data from sklearn
    breast_cancer_dataset = sklearn.datasets.load_breast_cancer()
    #loading the data to a data frame
    data_frame = pd.DataFrame(breast_cancer_dataset.data, columns = breast_cancer_dataset.feature_names)
    #adding the 'target' column to the data frame
    data_frame['label'] = breast_cancer_dataset.target
    # checking the distribution of Target Variable
    data_frame['label'].value_counts()
    data_frame.groupby('label').mean()
    X = data_frame.drop(columns= 'label', axis=1)
    Y = data_frame['label']
    from sklearn.model_selection import train_test_split
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2)
    from sklearn.linear_model import LogisticRegression
    model = LogisticRegression()
    #Training the Logistic Regression model using Training data
    model.fit(X_train, Y_train)
    #Testing the Logistic Regression model using Testing data
    model.score(X_test, Y_test)
    input_data = (19.07,24.81,128.3,1104,0.09081,0.219,0.2107,0.09961,0.231,0.06343,0.9811,1.666,8.83,104.9,0.006548,0.1006,0.09723,0.02638,0.05333,0.007646,24.09,33.17,177.4,1651,0.1247,0.7444,0.7242,0.2493,0.467,0.1038)
    # change the input data to a numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the numpy as we are predicting for one datapoint
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        print('The breast cancer is Malignant')
        
    else:
        print('The breast cancer is benign')
    return render(request,'output.html',{'prediction':prediction})

    