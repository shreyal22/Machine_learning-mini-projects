import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
df=pd.read_csv("movie.csv")
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
corpus = []
for i in range(0,df.shape[0]):
    review = re.sub('[^a-zA-Z]', ' ', df['text'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]    
    review = ' '.join(review)
    corpus.append(review)
from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer(max_features = 4000)
features=cv.fit_transform(corpus).toarray()
labels=df.iloc[:,0]
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels = le.fit_transform(labels)
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size = 0.20, random_state = 0)
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(features_train,labels_train)
labels_pred = lr.predict(features_test)
from sklearn.metrics import confusion_matrix
print(confusion_matrix(labels_test,labels_pred))
print(accuracy_score(labels_test,labels_pred))

