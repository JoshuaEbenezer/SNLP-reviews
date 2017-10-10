from collections import Counter
import csv
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import datasets, linear_model
from sklearn.model_selection import cross_val_score

#load the data frame
df = pd.read_csv('/home/josh/python/SNLP/src/truncate_data/zero_filter/test.csv')
#format usable in scikit
train = df.loc[:,'text'].values

#occurrence count and vectorizer, dict construction
count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(train)


#tfidf
tfidf_transformer = TfidfTransformer().fit(X_train_counts)
X = tfidf_transformer.transform(X_train_counts)
print (tfidf_transformer.vocabulary_)

# #word count
# X2 = (df.loc[:,'word_count'].values)

# print (X2.max())

#concatenate the two features
#X = np.concatenate((X1,X2))


# cont_var_y = df.loc[:,'useful'].values

# lab_enc = preprocessing.LabelEncoder()
# Y = lab_enc.fit_transform(cont_var_y)

# logreg = linear_model.LogisticRegression()
# scores = cross_val_score(logreg,X,Y,cv=5)

# print (scores)