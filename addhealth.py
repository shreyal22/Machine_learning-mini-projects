import pandas as pd
import numpy as np
from scipy.sparse.construct import random
from sklearn.metrics import accuracy_score
from sklearn.utils import axis0_safe_slice
df=pd.read_csv("addhealth.csv")
df.isnull().any(axis=0)
for i in df:
    df[i]=df[i].fillna(df[i].mode()[0])
features=df[['BIO_SEX','age','WHITE','BLACK','HISPANIC','NAMERICAN','ASIAN',
           'ALCEVR1','ALCPROBS1','marever1','cocever1','inhever1','cigavail',
           
           'DEP1','ESTEEM1']].values
labels=df["TREG1"].values
from sklearn.model_selection import train_test_split as tts
features_train, features_test, labels_train, labels_test = tts(features, labels, test_size = 0.20, random_state = 0)
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(features_train,labels_train)
labels_pred = lr.predict(features_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test,labels_pred))
print(accuracy_score(labels_test,labels_pred))
features_expel = df[["BIO_SEX","VIOL1"]].values
labels_expel = df["EXPEL1"].values
features_expel_train,features_expel_test,labels_expel_train,labels_expel_test=tts(features_expel,labels_expel,test_size=0.20,random_state=0)
from sklearn.linear_model import LogisticRegression
nlr=LogisticRegression()
nlr.fit(features_expel_train,labels_expel_train)
labels_expel_pred=nlr.predict(features_expel_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_expel_test,labels_expel_pred))
print(accuracy_score(labels_expel_test,labels_expel_pred))
