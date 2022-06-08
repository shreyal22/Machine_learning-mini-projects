import numpy as np
import pandas as pd
df=pd.read_csv('Female_Stats.csv')
features=df.iloc[:,1:].values
labels=df.iloc[:,[0]].values
df.isnull().any(axis=0)
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(features_train,labels_train)
pre=reg.predict(features_test)
import statsmodels.api as sm
features_sm = sm.add_constant(features)
est = sm.OLS(labels, features_sm)
est2 = est.fit()
print (est2.summary())
print (reg.coef_[0][0])
print(reg.coef_[0][1])

