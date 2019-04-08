from sklearn.utils import shuffle
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score



def predict_firstAuthor(df):
    pop_df = df
    #pop_df = df.unstack()
    #pop_df=pop_df.fillna(value=0)
    #pop_df = pop_df.reset_index()
    #pop_df=pop_df.reindex()


    #change column name
    pop_df=pop_df.rename(index=str,columns={"authors":"authors","sex":"sex",1:"First",2:"Second",3:"Third",4:"Fourth",5:"Fifth",6:"Sixth",7:
        "Seventh",8:"Eighth",9:"Ninth",10:"Tenth",11:"Eleventh",12:"Twelfth",13:"Thirteenth",14:"Fourthteen"})

    #change sex values
    sex={'Male':1,'Female':2, 'UKN':3}
    pop_df['sex']=[sex[item] for item in pop_df['sex']]

    #print(pop_df)
    Y = pop_df.First
    X = pop_df.drop(['authors','First'],axis=1)
    X_train,X_test,y_train,y_test = train_test_split(X,Y,test_size=0.33, random_state=42)
    print (X_train)
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train,y_train)
    print(clf.score(X_test,y_test))

    clf = svm.SVC(kernel = 'poly', gamma='scale')
    clf = clf.fit(X_train,y_train)
    print(clf.score(X_test,y_test))
    prediction = clf.predict(X_test)
    print(X_test[0:5],y_test[0:5])
    print(prediction[0:5])

