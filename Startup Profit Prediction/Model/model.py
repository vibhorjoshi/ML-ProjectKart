# -*- coding: utf-8 -*-
"""StartupProfitPrediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BRHtk73u5bteQMAUCATJ6nWu5fzbcgJ-

# **Startup Profit Prediction**

# Importing Libraries
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

"""# Reading the Data"""

df = pd.read_csv('/content/50_Startups.csv')
df

"""# Understanding the Data"""

df.dtypes

df.shape

df.size

df.columns

df.info()

df.max()

df.min()

df.describe()

df.corr()

df.nunique()

df.isnull().any()

"""# Visualization"""

import missingno as no
no.bar(df, color='pink')

sns.heatmap(df.isnull(), yticklabels='False', cmap='Blues')

df1 = df['State'].value_counts()
plt.pie(df1.values, labels=df1.index, autopct='%0.2f%%')
plt.title('States Pecentage', fontsize=15)
plt.show()

sns.distplot(df['Administration'], color='red')

sns.distplot(df['Marketing Spend'], color='y')

sns.heatmap(df.corr(), annot=True, fmt='.2f', square=True, cmap="RdYlBu")
plt.title("Correaltion", size=10)
plt.show()

plt.hist(df['Administration'],bins = 30, color='g')
plt.xlabel('Administration')
plt.ylabel('Profit')
plt.show()

sns.pairplot(df)

plt.xlabel("Administration")
plt.ylabel("Profit")
plt.title("Administration vs Profit")
plt.scatter(df["Administration"], df.Profit, color="red", marker="*")
plt.show()

plt.xlabel("Marketing Spend")
plt.ylabel("Profit")
plt.title("Marketing Spend vs Profit")
plt.scatter(df["Marketing Spend"], df.Profit, color="y", marker="+")
plt.show()

"""# Splitting of Dataset into Dependent and Independent variables"""

x = df.drop(["State","Profit"], axis=1)
y = df["Profit"]

"""# Training and Testing the Data"""

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=10)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(xtrain, ytrain)

"""# Prediction"""

ypred_train = model.predict(xtrain)
ypred_test = model.predict(xtest)

"""# Performance"""

df = pd.DataFrame(ypred_test, ytest)
df.head()

"""# Accuracy"""

from sklearn import metrics
print("Accuracy of training data:", metrics.r2_score(ytrain, ypred_train)*100)
ac = metrics.r2_score(ytest, ypred_test)*100
print("Accuracy of testing data:", ac)

from sklearn.metrics import mean_squared_error
mse = mean_squared_error(ytest, ypred_test)
print("Mean Square Error:", mse)

"""# Plotting Regression Line"""

plt.figure(figsize=(12,8))
plt.scatter(ytrain, ypred_train, c='r', marker='*')
plt.scatter(ytest, ypred_test, c='b', marker='^')
plt.plot(ytest, ypred_test, c='y', label = "Regression Line")
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.legend(['Regression Line', 'Training data', 'Test data'])
plt.show()

p=model.predict([[167750,105145.55,437934.54]])
p

"""# Saving the Model"""

import pickle 
pickle.dump(model, open('model.pkl', 'wb'))
