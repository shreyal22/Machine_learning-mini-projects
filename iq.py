import numpy as np
import pandas as pd
df=pd.read_csv('IQ_Size.csv')
features=df.iloc[:,1:].values
labels=df.iloc[:,[0]].values
df.isnull().any(axis=0)
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test=train_test_split(features,labels,test_size=0.2,random_state=0)
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(features_train,labels_train)
pre=reg.predict([[90,70,150]])
print(pre)
import statsmodels.api as sm
import numpy as np
features = sm.add_constant(features)
features_optimal = features[:, [0,1,2,3]]
while (True):
    regressor_OLS = sm.OLS(endog = labels,exog =features_optimal).fit()
    p_values = regressor_OLS.pvalues
    if p_values.max() > 0.05 :
        features_optimal = np.delete(features_optimal, p_values.argmax(),1)
    else:
        break
print (features_optimal.columns)
