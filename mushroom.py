import pandas as pd
data = pd.read_csv("mushrooms.csv")
features = data.iloc[:,[5,-2,-1]]
labels = data.iloc[:,0].values
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
le = LabelEncoder()
labels = le.fit_transform(labels)
cTransformer = ColumnTransformer([('encoder', OneHotEncoder(), [0,1,2])], remainder = 'passthrough')
features = cTransformer.fit_transform(features).toarray()
from sklearn.model_selection import train_test_split
features_train,features_test,labels_train,labels_test = train_test_split(features,labels,test_size=0.25,random_state=0)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=5, p=2)
classifier.fit(features_train,labels_train)
pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(labels_test,pred)
print(cm)
print (classifier.score(features_test,labels_test))#99.5%
