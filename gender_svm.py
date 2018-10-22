import csv
import pickle

import pandas as pd
import numpy as np
import re

from sklearn.model_selection import StratifiedKFold, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.utils import shuffle
from sklearn.feature_extraction import DictVectorizer
from sklearn import svm
#import matplotlib.pyplot as plt

TRAIN_SPLIT = 0.8

def gender_features(name):
    #print(type(name))
    name = name.lower()
    return{
    'first-letter': name[0], # First letter
    'first2-letters': name[0:2], # First 2 letters
    'first3-letters': name[0:3], # First 3 letters
    'last-letter': name[-1],
    'last2-letters': name[-2:],
    'last3-letters': name[-3:],
    'first_letter_vowel':extract_vowel_bool(name[0]),
    'last_letter_vowel':extract_vowel_bool(name[-1]),
    #'first_2letter_vowel':extract_vowel_bool(name[0:2]),
    #'last_2letter_vowel':extract_vowel_bool(name[-2:]),
    }


def readName(pathFile,*args):

    names = pd.read_csv(pathFile)

    for a in args:
        #names.drop(['Unnamed: 0'],axis=1, inplace=True )
        names.drop(a,axis=1,inplace=True)
    names = names.values[:, 0:]

    #print(type(names))
    return names


def extract_vowel(name):
    name = name.lower()
    return re.sub(r'[^AEIOU]', '', name, flags=re.IGNORECASE)


def extract_vowel_bool(name):
    name = name.lower()
    if re.search(r'[AEIOUY]',name,flags=re.IGNORECASE):
        return 1
    else:
        return 0

def extract_conson_bool(name):
    name = name.lower()
    if re.search(r'[^AEIOU]',name,flags=re.IGNORECASE):
        return 1
    else:
        return 0

def prepare_dataFrame(dataframe):
    gender_feat = np.vectorize(gender_features)
    X = gender_feat(dataframe[:, 0])
    y = dataframe[:, 1]
    print ("Name: %s, features=%s, gender=%s" % (dataframe[5][0], X[5], y[0]))
    X, y = shuffle(X, y)
    X_train, X_test = X[:int(TRAIN_SPLIT * len(X))], X[int(TRAIN_SPLIT * len(X)):]
    y_train, y_test = y[:int(TRAIN_SPLIT * len(y))], y[int(TRAIN_SPLIT * len(y)):]
    return X_train,X_test,y_train,y_test

def train(X_train,X_test,y_train,y_test):
    vectorizer = DictVectorizer()
    vectorizer.fit(X_train)
    clf = svm.SVC(kernel='linear', C=1,gamma='scale')
    clf.fit(vectorizer.transform(X_train), y_train)
    print('accuracy training set ',clf.score(vectorizer.transform(X_train), y_train))
    print ('accuracy test set ',clf.score(vectorizer.transform(X_test), y_test))
    return clf,vectorizer



dataframe=readName('/Users/derib/Desktop/allConcatName.csv','Unnamed: 0','index')
Xtrain,X_test,y_train,y_test=prepare_dataFrame(dataframe)
clf=train(Xtrain,X_test,y_train,y_test)



vectorizer = DictVectorizer()
gender_features = np.vectorize(gender_features)
gender_features(["George", "Emma"])


allName=readName('/Users/derib/Desktop/nameList.csv','index')
#print((allName[:,0]))
df = pd.DataFrame()
df['name']=allName[:,0]
#print(df)
# print(type(clf[0]),type(clf[1]))
# print(clf[0].predict(clf[1].transform(gender_features(allName[:,0]))))


df['prediction']=clf[0].predict(clf[1].transform(gender_features(allName[:,0])))
#print(df)
df['real data']=allName[:,1]
df.to_csv('/Users/derib/Desktop/predictionNameSVM.csv')
# print(allName)

#plot()



# print(clf.predict(vectorizer.transform(gender_features(allName[:,0]))))
#
# # Accuracy on training set
#print (clf.score(vectorizer.transform(X_train), y_train))   # 0.988292554591 = 98.8% accurate
#
# # Accuracy on test set
#print (clf.score(vectorizer.transform(X_test), y_test))
