# -*- coding: utf-8 -*-
"""Task_14.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/Sourav61/Goeduhub-Assignments/blob/main/Task_14.ipynb
"""

from google.colab import drive
drive.mount('/content/drive')

"""Author: <a href = "https://github.com/Sourav61">Sourav Pahwa</a>
<br>ID: GO_STP_13420

Practice KNN - We have a dataset that contains multiple user's information through the social network who are interested in buying SUV Car or not. 

DataSet-Click Here for Download <a href="https://drive.google.com/file/d/1AyN2ACOsNk4_YdpZVHpODGAb3YQh5LHp/view">user_data.csv </a>
"""

import numpy as np
import pandas as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt
import missingno as msno
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("User_Data.csv")

df.head(10)

df.tail(10)

df.keys

df.info()

df.describe(include="all")

df.describe(include="object")

df.describe().style.background_gradient(cmap='CMRmap_r', low=0, high=0, axis=0, subset=None, text_color_threshold=0.408, vmin=None, vmax=None)

def inspect_data(data):
    return pd.DataFrame({"Data Type":data.dtypes,"No of Levels":data.apply(lambda x: x.nunique(),axis=0), "Levels":data.apply(lambda x: str(x.unique()),axis=0)})
inspect_data(df)

df.kurt()

df.skew()

df.keys()

df.columns

df.axes

df.items

df.ndim

df.boxplot(rot=45)
plt.show()

df.hist(figsize=(15,20),xrot=45,yrot=45)
plt.show()

df.dtypes

df.duplicated().any()

df.duplicated().sum()

df.isna()

df.isnull().any()

df.isnull().sum()

msno.bar(df.sample(400),color=("#CC99FF"))
plt.show()

msno.matrix(df.sample(400),color=(1, 0, 1))
plt.show()

df.corr()

fig = plt.figure(figsize = (12,10))
sns.heatmap(df.corr(), cmap='CMRmap', annot = True) 
plt.show()

corr = df.corr()
sns.heatmap((corr),
xticklabels=corr.columns.values,
yticklabels=corr.columns.values,cmap='gnuplot2_r',annot=False,fmt=".2g")
plt.title('Heatmap of Correlation Matrix', fontsize=20)
corr

df.groupby('Purchased').mean()

df.groupby('Purchased').var()

df.groupby('Purchased').std()

df.groupby('Purchased').cov()

plt.figure(figsize=(14,14))
sns.heatmap(df.cov(), annot=True, fmt =".2f",square=True,cmap='flare_r')
plt.title("Covariation",fontsize = 15)
plt.show()

df.columns

sns.pairplot(df,
             x_vars = ['Age', 'EstimatedSalary', 'Purchased'],
             y_vars = ['Age', 'EstimatedSalary', 'Purchased'],
       diag_kind='kde',hue='Purchased', palette="autumn"
             )
plt.show()

plt.rcParams['figure.figsize'] = (15, 5)
plt.style.use('seaborn-dark')

plt.subplot(1, 2, 1)
sns.countplot(df['User ID'])
plt.show()

plt.xlabel('User ID', fontsize = 15)

plt.subplot(1,2,2)
sns.distplot(df["User ID"], bins = 20)
plt.show()

plt.rcParams['figure.figsize'] = (15, 5)
plt.style.use('ggplot')

plt.subplot(1, 2, 1)
sns.countplot(df['Gender'])
plt.show()

plt.xlabel('Gender', fontsize = 15)

plt.subplot(1, 2, 2)
df['Gender'].value_counts().plot(kind = 'pie', explode = [0, 0.1], autopct = '%.2f%%', startangle = 90,
                                       labels = ['0','1'], shadow = True, pctdistance = 0.5)
plt.show()

plt.rcParams['figure.figsize'] = (15, 5)
plt.style.use('ggplot')

plt.subplot(1, 2, 1)
sns.countplot(df['Age'])
plt.show()

plt.xlabel('Age', fontsize = 15)

plt.subplot(1, 2, 2)
sns.distplot(df["Age"], bins = 20)
plt.show()

plt.rcParams['figure.figsize'] = (15, 5)
plt.style.use('ggplot')

plt.subplot(1, 2, 1)
sns.countplot(df['EstimatedSalary'])
plt.show()

plt.xlabel('EstimatedSalary', fontsize = 15)

plt.subplot(1, 2, 2)
sns.distplot(df["EstimatedSalary"], bins = 20)
plt.show()

sns.boxplot(y='Age', x='Gender', data = df, palette = 'flare_r')
plt.show()

plt.figure(figsize=(15,10))
sns.swarmplot(y = "Age", x = "Gender", data = df, palette = 'cool')
plt.show()

plt.rcParams['figure.figsize'] = (15, 5)
plt.style.use('seaborn-bright')

sns.boxplot(y='Age', x='Gender', data = df, palette = 'PuBu')
sns.swarmplot(y='Age', x='Gender', data = df, palette = 'inferno')
plt.show()

plt.rcParams['figure.figsize'] = (15, 5)
plt.style.use('seaborn-dark-palette')

fig, axarr = plt.subplots(3,2, figsize=(20,20))

sns.stripplot(y='Age', x='Gender', data=df, hue=None, ax=axarr[0][0])
sns.stripplot(y='Purchased', x='Age', data=df, hue=None, ax=axarr[0][1])
sns.stripplot(y='EstimatedSalary', x='Purchased', data=df, hue=None, ax=axarr[1][0])
sns.stripplot(y='Age', x='EstimatedSalary', data=df, hue=None, ax=axarr[1][1])
sns.stripplot(x='Gender', y='Purchased', data=df, hue=None, ax=axarr[2][0])
sns.stripplot(y='EstimatedSalary', x='Gender', data=df, hue=None,  ax=axarr[2][1])

plt.show()

fig = px.histogram(df, 
                   x='Age', 
                   marginal='box', 
                   nbins=47, 
                   title='Distribution of Age')
fig.update_layout(bargap=0.1)
fig.show()

fig = px.histogram(df, 
                   x='EstimatedSalary', 
                   marginal='box', 
                   color='Gender',
                   color_discrete_sequence=['tomato','darkcyan'], 
                   title='Gender Classification')
fig.update_layout(bargap=0.1)
fig.show()

fig = px.histogram(df, 
                   x='Age', 
                   marginal='box', 
                   color='Gender', 
                   color_discrete_sequence=['darkgreen', 'aquamarine'], 
                   title='Expenses according to Age')
fig.update_layout(bargap=0.1)
fig.show()

fig = px.scatter(df, 
                 x='Age', 
                 y='EstimatedSalary', 
                 color='Purchased', 
                 opacity=0.7, 
                 hover_data=['Gender'], 
                 title='Age VS Estimated Salary')
fig.update_traces(marker_size=5)
fig.show()

fig = px.scatter(df, 
                 x='EstimatedSalary', 
                 y='User ID', 
                 color='Purchased', 
                 opacity=0.6, 
                 hover_data=['Age'], 
                 title='Estimated Salary VS UserID')
fig.update_traces(marker_size=5)
fig.show()

plt.rcParams['figure.figsize'] = (15, 5)
plt.style.use('ggplot')

plt.subplot(1, 3, 1)
sns.countplot(df['Purchased'])
plt.show()

plt.xlabel('Purchased', fontsize = 15)

plt.subplot(1, 3, 2)
df['Purchased'].value_counts().plot(kind = 'pie', explode = [0, 0.1], autopct = '%.2f%%', startangle = 90,
                                       labels = ['0','1'], shadow = True, pctdistance = 0.5)
plt.legend()

plt.subplot(1, 3, 3)
sns.distplot(df["Purchased"], bins = 20)
plt.show()

px.histogram(df, x='Gender', color='Purchased', title='Purchased Or Not')

dummies = pd.get_dummies(df.Gender)

x = df.drop(['Purchased','Gender'], axis = 'columns')
y = df['Purchased']

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.2, random_state = 9)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)

knn.fit(xtrain, ytrain)

from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

pred = knn.predict(xtest)

cm = confusion_matrix(ytest, pred)
print(cm,"\n")

print(accuracy_score(ytest, pred),"\n")

print(classification_report(ytest, pred))