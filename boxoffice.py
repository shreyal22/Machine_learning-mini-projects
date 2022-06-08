import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
df=pd.read_csv('Box_Office.csv')
#bahubali

b_label=df.iloc[:,1:2].values
b_feature=df.iloc[:,0:1].values
bfeature_train,bfeature_test,blabel_train,blabel_test=train_test_split(b_feature,b_label,test_size=0.2,random_state=0)
regressor1=LinearRegression()
regressor1.fit(bfeature_train,blabel_train)
print("bahubali box office collection is")
print(regressor1.predict([[10]]))

#dangal

d_label=df.iloc[:,2:].values
d_feature=df.iloc[:,0:1].values
dfeature_train,dfeature_test,dlabel_train,dlabel_test=train_test_split(d_feature,d_label,test_size=0.2,random_state=0)
regressor2=LinearRegression()
regressor2.fit(dfeature_train,dlabel_train)
print("dangal box office collection is")
print(regressor2.predict([[10]]))

