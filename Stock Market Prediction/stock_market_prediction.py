# -*- coding: utf-8 -*-
"""Stock Market Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RYWu0rVxiP3o3SWKX6R0qd-T2BJ_1Omc

# Stock Market Prediction And Forecasting Using Stacked LSTM

LSTM: Long Short Term Memory

### Steps Invloved


1. Collect the Stock Data [ Apple Comp Stock Price ].
2. Preprocess the data - train and test.
3. Create and Stacked LSTM Model.
4. Predict the test data and plot the output.
5. predict the next 30 days and plot the output.

# **pandas-datareader**:  
pandas-datareader is a remote data access for pandas, ie provides lot 
of libraries to access data. Eg. we will be using Tiingo.

* [pandas-datareader docs](https://pandas-datareader.readthedocs.io/en/latest/)



---



# **Tiingo** :
Tiingo is a tracing platform that provides a data api with historical end-of-day prices on equities, mutual funds and ETFs etc

* [Tiingo](https://pandas-datareader.readthedocs.io/en/latest/remote_data.html#remote-data-tiingo)
*   [Tiingo Website](https://www.tiingo.com/)

# Step One : Collect the data.
"""

# import data reader
import pandas_datareader as pdr

# key must be hidden
key = 'xxxxxxxxxx'

# get the entire Apple data into a data frame
df = pdr.get_data_tiingo('AAPL', api_key=key)

df.to_csv('AAPL.csv')

df.head()

df.tail()

"""## Performing stock prediction on the close column"""

# reseting the index. ie giving index values
df_1 = df.reset_index()

df_1.head()

# Pick up close column
df_1 = df.reset_index()['close']

df_1.shape

"""## plotting the data frame"""

import matplotlib.pyplot as plt
plt.plot(df_1)

df_1

"""### LSTM is very sensitive to scalar data eg. 129.67
### so we convert it into min max scalar which transform data between 0-1. 
"""

import numpy as np
from sklearn.preprocessing import MinMaxScaler

# https://stackoverflow.com/questions/18691084/what-does-1-mean-in-numpy-reshape

scalar = MinMaxScaler(feature_range=(0,1)) # scaling value
df_1 = scalar.fit_transform(np.array(df_1).reshape(-1,1))  # reshape to provide input to fit_Transform

df_1.shape

df_1

"""# Step 2 :  Preprocess the data

This is a time series data.

Cross validation and random seed works well on linear data.

So for time series data we got to process by dividing the data into train and test.

eg. 70% data is the training data and 30% data is our test data.

### 1.   Splitting the data into train and test
"""

training_data_size = int(len(df_1)*0.70)
print(training_data_size)

# training data size is 70% of the data frame
# testing data size is 30% of data frame
testing_data_size= len(df_1) - training_data_size
print(testing_data_size)

# 0 to 879 will be training data
training_data = df_1[0:training_data_size] 
print(len(training_data))

# from 879 to end will be test data
testing_data = df_1[training_data_size : len(df_1)]
print(len(testing_data))

"""
## 2.   Calculate X_data , y_data

"""

def create_dataset(dataset , number_of_independent_feature = 1):
  X_data, y_data = [], []

  print(len(dataset)) # 879
  print(number_of_independent_feature-1) # 99
  print(len(dataset)-number_of_independent_feature-1) # 778

  for i in range(len(dataset)-number_of_independent_feature-1):
    # for i in range(778) will go upto 777
    sliced_dataset = dataset[i:(i+number_of_independent_feature),0] # 0 is the axis
    # print(sliced_dataset)
    X_data.append(sliced_dataset)
    y_data.append(dataset[i+number_of_independent_feature,0])
  
  return np.array(X_data), np.array(y_data)

number_of_independent_feature = 100
X_train, y_train = create_dataset(training_data, number_of_independent_feature)
X_test, y_test = create_dataset(testing_data, number_of_independent_feature)

# print("X_train data is: ",X_train)
# print('\n')
# print("y_train data is: ",y_train)

# print("X_test data is: ",X_test)
# print('\n')
# print("y_test data is: ",y_test)

print(X_train.shape)
print(y_train.shape)

print(X_test.shape)
print(y_test.shape)

"""# Step 3: Create and Stacked LSTM Model.

The input to every LSTM layer must be three-dimensional.

The three dimensions of this input are:

Samples. One sequence is one sample. A batch is comprised of one or more samples.

Time Steps. One time step is one point of observation in the sample.

Features. One feature is one observation at a time step.

#### Before creating any LSTM model we have to reshape out X train and X test.

#### Our X data set is in 2 dimension. Convert it into 3D by adding 1.

### third dimension will be our feature.
"""

X_train = X_train.reshape(X_train.shape[0],X_train.shape[1],1)
X_test = X_test.reshape(X_test.shape[0],X_test.shape[1],1)

print(X_train.shape)
print(X_test.shape)

"""

##    Create Stacked LSTM Model

"""

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import LSTM

model = Sequential()
model.add(LSTM(50,return_sequences=True,input_shape=(100,1))) # X train shape is 778,100,1 so we give 100, 1
# stacked LSTM. One layer after the other
model.add(LSTM(50,return_sequences=True))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

model.summary()

model.fit(X_train, y_train, validation_data=(X_test,y_test), epochs=100, batch_size=64, verbose=2)

"""# Step 4 : Predict the test data and plot the output."""

import tensorflow as tf

## Prediction
train_predict = model.predict(X_train)
test_predict = model.predict(X_test)

# print("prediction on X train is: ",train_predict)
# print("\n")
# print("prediction on X_test is",test_predict)

# we had used Min max scalar so we got to inverse it back to original form

train_predict = scalar.inverse_transform(train_predict)
test_predict = scalar.inverse_transform(test_predict)

"""## Regression Metrics for Machine Learning:

*   Regression refers to predictive modeling problems that involve predicting a numeric value.
*   Predictive modeling is the problem of developing a model using historical data to make a prediction on new data where we do not have the answer.


---


### Metrics for Regression:
*   Mean Squared Error : Mean Squared Error, or MSE for short, is a popular error metric for regression problems.

-   mean_squared_error(expected, predicted)

---



[Regression Metrics](https://machinelearningmastery.com/regression-metrics-for-machine-learning/)
"""

import math
from sklearn.metrics import mean_squared_error

# for train data set
(math.sqrt(mean_squared_error(y_train, train_predict)))

# for test data
math.sqrt(mean_squared_error(y_test, test_predict))

"""
### Time Series Prediction with LSTM Recurrent Neural Networks in Python with Keras 

Because of how the dataset was prepared, we must shift the predictions so that they align on the x-axis with the original dataset. Once prepared, the data is plotted, showing the original dataset in blue, the predictions for the training dataset in green, and the predictions on the unseen test dataset in red.


[Plotting](https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/)



---

"""

# plotting
# time step is same as look_back. 99 independent and 1 dependent feature
look_back = 100
# shift train predictions for plotting
trainPredictPlot = np.empty_like(df_1)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(train_predict)+look_back, :] = train_predict
# shift test predictions for plotting
testPredictPlot = np.empty_like(df_1)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(train_predict)+(look_back*2)+1:len(df_1)-1, :] = test_predict
# plot baseline and predictions
plt.plot(scalar.inverse_transform(df_1))
plt.plot(trainPredictPlot)
plt.plot(testPredictPlot)
plt.show()

"""# Step 5: predict the next 30 days and plot the output."""

# for getting 31 day prediction i need to have previous 30days

len(testing_data)

X_input = testing_data[278:].reshape(1,-1)

X_input.shape

X_input

# converting into a list.
temp_input = list(X_input)
print(temp_input)

temp_input = temp_input[0].tolist() # Pandas tolist() is used to convert a series to list.
print(temp_input)

# predicting for next 30 days

from numpy import array

list_output = []
n_steps = 100
i = 0

# calulate for 30 days
while(i<30):

  if(len(temp_input) > 100 ):
    # when my temp_input has more than one 100 value then start from 1 to end. ie 1 to 101
    X_input = np.array(temp_input[1:])
    print("{} day input is {} (100)".format(i,X_input))
    print("\n")

    # we got to reshape before performing prediction
    X_input = X_input.reshape(1,-1) # New shape as (1,-1). i.e, row is 1, column unknown.
    X_input = X_input.reshape((1,n_steps,1))

    print("X_input for greater than 100 is",X_input)
    print("\n")

    y_hat = model.predict(X_input,verbose=0)
    print("{} day input is {} (100)".format(i,y_hat))
    print("\n")

    temp_input.extend(y_hat[0].tolist())

    temp_input = temp_input[1:]

    print("temp input is(100): ", temp_input)
    print("\n")


    list_output.extend(y_hat.tolist())

    i += 1

  else:
    X_input = X_input.reshape((1,n_steps,1))
    y_hat = model.predict(X_input,verbose=0)

    print("{} day input is {}".format(i,y_hat))
    print("\n")

    temp_input.extend(y_hat[0].tolist())

    print("temp input is: ", temp_input)
    print("\n")


    list_output.extend(y_hat.tolist())

    i += 1 

print("Print the list output is: ",list_output)

"""# Plotting"""

# test day has previous 100 days
day = np.arange(1,101)
# have to predict next 100 days
day_pred = np.arange(101,131)

import matplotlib.pyplot as plt

len(df_1)

# 1157 because total length of data frame is 1257. and we have taken the previous 100 data
# so previous 100 means it start from 1157 to 1257
plt.plot(day,scalar.inverse_transform(df_1[1157: ]))
plt.plot(day_pred,scalar.inverse_transform(list_output))

# the orange line shows the prediction

# complete op

df_2 = df_1.tolist()
df_2.extend(list_output)
plt.plot(df_2[1200: ])