import pandas as pd
data=pd.read_table("amazon_cells_labelled.txt",names=["Review","Liked"])
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import re
corpus = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', data['Review'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]    
    review = ' '.join(review)
    corpus.append(review)
print(corpus)
print(len(corpus))
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features =1500)
features = cv.fit_transform(corpus).toarray() # 1500 columns
labels = data.iloc[:, 1].values
print(features.shape)
print(labels.shape)
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = \
train_test_split(features, labels, test_size = 0.20, random_state = 0)
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(features_train, labels_train)
labels_pred = classifier.predict(features_test)
from sklearn.metrics import confusion_matrix
cm_knn = confusion_matrix(labels_test, labels_pred)
print(cm_knn) 
