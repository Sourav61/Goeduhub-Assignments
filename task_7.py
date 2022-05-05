# -*- coding: utf-8 -*-
"""Task_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Sourav61/Goeduhub-Assignments/blob/main/Task_07.ipynb
"""

from google.colab import drive
drive.mount('/content/drive')

"""Author: <a href = "https://github.com/Sourav61">Sourav Pahwa</a>
<br>ID: GO_STP_13420

<b>Task 7: In this task we have to find the students scores based on their study hours. This is a simple Regression problem type because it has only two variables.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("StudentHoursScores.csv")

df.head(10)

df.tail(10)

df.info()

df.describe(include="all")

df.axes

df.columns

df.dtypes

df.boxplot()

df.duplicated()

df.kurt()

df.skew()

df.keys()

df.isna()

df.corr()

df.nunique()

fig = plt.figure(figsize = (12,10))
sns.heatmap(df.corr(), cmap='gist_rainbow', annot = True) 
plt.plot()

type(df)

a = df.iloc[:,:-1]
b = df.iloc[:,1]
plt.xlabel("Hours")
plt.ylabel("Scores")
plt.scatter(a,b,color='m',marker='*')
plt.show()

print(a.shape,b.shape)

a.head()

b.head()

from sklearn.model_selection import train_test_split

a_train, a_test, b_train, b_test = train_test_split(a, b, test_size=0.3, random_state=1)

a_train.shape

a_test.shape

b_train.shape

b_test.shape

from sklearn.linear_model import LinearRegression
model = LinearRegression()

model.fit(a_train,b_train)

pred = model.predict(a_test)

pred

print(b_test)

print(a_test)

model.coef_

model.intercept_

plt.scatter(a_train, b_train, color="m")
plt.plot(a_train, model.predict(a_train))
plt.show()

from sklearn.metrics import r2_score, mean_squared_error
print("accuracy is: ", r2_score(b_test,pred))

print(mean_squared_error(b_test,pred))