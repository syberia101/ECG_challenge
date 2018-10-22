import pandas as pd
import numpy as np
import re
from sklearn.pipeline import Pipeline, FeatureUnion

names = pd.read_csv('/Users/derib/Desktop/allConcatName.csv')
names.drop(['Unnamed: 0',  'index'],axis=1, inplace=True )
#print(names)


# Get the data out of the dataframe into a numpy matrix and keep only the name and gender columns
names = names.values[:, 0:]

#print (names)

# We're using 80% of the data for training
TRAIN_SPLIT = 0.8


def features(name):
    name = name.lower()
    print(type(name),name.lower())
    print('why')
    return {
        'first-letter': name[0], # First letter
        'first2-letters': name[0:2], # First 2 letters
        'first3-letters': name[0:3], # First 3 letters
        'last-letter': name[-1],
        'last2-letters': name[-2:],
        'last3-letters': name[-3:],
        'vowel':extract_vowel(name[:]),
        'conson':extract_conson(name[:])
    }

#print (features("John"))

def extract_conson(name):
    name = name.lower()
    return re.sub(r'[AEIOU]', '', name, flags=re.IGNORECASE)

def extract_vowel(name):
    name = name.lower()
    return re.sub(r'[^AEIOU]', '', name, flags=re.IGNORECASE)

# #print('feature 2',features_2('Helene'))
# # Vectorize the features function
#
# features = np.vectorize(features)
# print (features(["Anna", "Hannah", "Paul"]))
#
# # features_2= np.vectorize(features_2)
# # print (features_2(["Anna", "Hannah", "Paul"]))
#
# # Extract the features for the whole dataset
# X = features(names[:, 0]) # X contains the features
#
# #X2 = features_2(names[:,0])
#
#
# #combined_features = FeatureUnion([("nbChar", features), ("vowel", features_2)])
#
# # Get the gender column
# y = names[:, 1]           # y contains the targets
#
# # Test if we built the dataset correctly
# print ("Name: %s, features=%s, gender=%s" % (names[5][0], X[5], y[0]))
#
# from sklearn.utils import shuffle
# X, y = shuffle(X, y)
# X_train, X_test = X[:int(TRAIN_SPLIT * len(X))], X[int(TRAIN_SPLIT * len(X)):]
# y_train, y_test = y[:int(TRAIN_SPLIT * len(y))], y[int(TRAIN_SPLIT * len(y)):]
#
# # Check to see if the datasets add up
# print (len(X_train), len(X_test), len(y_train), len(y_test))
#
# from sklearn.feature_extraction import DictVectorizer
#
# print ('features ',features(["Mary", "John"]))
# vectorizer = DictVectorizer()
# vectorizer.fit(X_train)
#
# transformed = vectorizer.transform(features(["Mary", "John"]))
# print (transformed)
#
# print (type(transformed)) # <class 'scipy.sparse.csr.csr_matrix'>
# print (transformed.toarray()[0][12])    # 1.0
# print (vectorizer.feature_names_[12])
#
#
# from sklearn.tree import DecisionTreeClassifier
#
# clf = DecisionTreeClassifier()
# clf.fit(vectorizer.transform(X_train), y_train)
#
# print('titititi')
features(["George", "Emma"])

# Accuracy on training set
# print (clf.score(vectorizer.transform(X_train), y_train))   # 0.988292554591 = 98.8% accurate
#
# # Accuracy on test set
# print (clf.score(vectorizer.transform(X_test), y_test))   # 0.863246514075 = 86.3% accurate
#
#
# from sklearn import svm
#
# clf = svm.SVC(gamma='scale')
# clf.fit(vectorizer.transform(X_train), y_train)
#
# print(clf.predict(vectorizer.transform(features(["Ian", "Peter"]))))
#
# # Accuracy on training set
# print (clf.score(vectorizer.transform(X_train), y_train))   # 0.988292554591 = 98.8% accurate
#
# # Accuracy on test set
# print (clf.score(vectorizer.transform(X_test), y_test))   # 0.863246514075 = 86.3% accurate


