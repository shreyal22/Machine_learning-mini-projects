import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('bluegills.csv')
features=df.iloc[:,0:1]
labels=df.iloc[:,1:]
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(features_train,labels_train)
print(reg.predict([[5]])) #175.50
print(reg.score(features_train, labels_train))
from sklearn.preprocessing import PolynomialFeatures
higher_degree_gen = PolynomialFeatures(degree = 4)
features_poly = higher_degree_gen.fit_transform(features)
regressor_poly = LinearRegression()
regressor_poly.fit(features_poly, labels)
print(regressor_poly.predict(higher_degree_gen.fit_transform([[5]])))#165.92
print(regressor_poly.score(features_poly, labels))