

# Samnple Workflow
From this helpful guide: https://www.kaggle.com/vinothan/titanic-model-with-90-accuracy

### Identify Missing Data: Populate or Delete

Load in initial datasets

    train_df=pd.read_csv("../input/digit-recognizer/train.csv")
    test_df=pd.read_csv("../input/digit-recognizer/test.csv")

    train_df.head()

Dependencies

    import numpy as np 
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    warnings.filterwarnings('ignore')
    %matplotlib inline

Renders a bar chart of which data is the most missing. 

    def missingdata(data):
    total = data.isnull().sum().sort_values(ascending = False)
    percent = (data.isnull().sum()/data.isnull().count()*100).sort_values(ascending = False)
    ms=pd.concat([total, percent], axis=1, keys=['Total', 'Percent'])
    ms= ms[ms["Percent"] > 0]
    f,ax =plt.subplots(figsize=(8,6))
    plt.xticks(rotation='90')
    fig=sns.barplot(ms.index, ms["Percent"],color="green",alpha=0.8)
    plt.xlabel('Features', fontsize=15)
    plt.ylabel('Percent of missing values', fontsize=15)
    plt.title('Percent missing data by feature', fontsize=15)
    return ms

    missingdata(train_df)

Notice that the Cabin value ins missing in ~80% of columns. Might as well delete it. 

    drop_column = ['Cabin']
    train_df.drop(drop_column, axis=1, inplace = True)
    test_df.drop(drop_column,axis=1,inplace=True)

In this case, populate missing data with a mean. 
Age is only missing in ~15% of cases - and I suspect will be useful. Keep it, and populate with the median. 

    test_data['Age'].mean()
    train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace = True)
    test_df['Fare'].fillna(test_df['Fare'].median(), inplace = True)

    test_df['Age'].fillna(test_df['Age'].median(), inplace = True)
    train_df['Age'].fillna(train_df['Age'].median(), inplace = True)

Checking for nan values in any of our tables:

    print('check the nan value in train data')
    print(train_df.isnull().sum())
    print('___'*30)
    print('check the nan value in test data')
    print(test_df.isnull().sum())

### Feature Engineering

Box Cox transform - make the data more like a normal distribution. 
We'll want to do this to all data, training and test:

    all_data=[train_data, test_data]

Some ideas for engineered features: titles, family size

    for dataset in all_data:
        dataset['FamilySize'] = dataset['SibSp'] + dataset['Parch'] + 1

        import re
    # Define function to extract titles from passenger names
    def get_title(name):
        title_search = re.search(' ([A-Za-z]+)\.', name)
        # If the title exists, extract and return it.
        if title_search:
            return title_search.group(1)
        return ""
    # Create a new feature Title, containing the titles of passenger names
    for dataset in all_data:
        dataset['Title'] = dataset['Name'].apply(get_title)
    # Group all non-common titles into one single grouping "Rare"
    for dataset in all_data:
        dataset['Title'] = dataset['Title'].replace(['Lady', 'Countess','Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

        dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
        dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
        dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')

    ## create bin for age features
    for dataset in all_data:
        dataset['Age_bin'] = pd.cut(dataset['Age'], bins=[0,12,20,40,120], labels=['Children','Teenage','Adult','Elder'])

    ## create bin for fare features
    for dataset in all_data:
        dataset['Fare_bin'] = pd.cut(dataset['Fare'], bins=[0,7.91,14.45,31,120], labels=['Low_fare','median_fare', 'Average_fare','high_fare'])

    ### for our reference making a copy of both DataSet start working for copy of dataset
    traindf=train_df
    testdf=test_df
    
    all_dat=[traindf,testdf]
    
    for dataset in all_dat:
        drop_column = ['Age','Fare','Name','Ticket']
        dataset.drop(drop_column, axis=1, inplace = True)
    
    drop_column = ['PassengerId']
    traindf.drop(drop_column, axis=1, inplace = True)

Converting bins of categorical features into dummy values

    traindf = pd.get_dummies(traindf, columns = ["Sex","Title","Age_bin","Embarked","Fare_bin"], prefix=["Sex","Title","Age_type","Em_type","Fare_type"])
    testdf = pd.get_dummies(testdf, columns = ["Sex","Title","Age_bin","Embarked","Fare_bin"], prefix=["Sex","Title","Age_type","Em_type","Fare_type"])

### Correlations Between Features

Heatmap, very nice

    sns.heatmap(traindf.corr(),annot=True,cmap='RdYlGn',linewidths=0.2) #data.corr()-->correlation matrix
    fig=plt.gcf()
    fig.set_size_inches(20,12)
    plt.show()

Pairplots

    g = sns.pairplot(data=train_df, hue='Survived', palette = 'seismic', size=1.2,diag_kind = 'kde',diag_kws=dict(shade=True),plot_kws=dict(s=10) )
    g.set(xticklabels=[])

### The Models

This is a supervised learning / classification & regression problem. Our options: 

- Logistic Regression
- KNN
- Support Vector Machines
- Naive Bayes Classifier
- Decision Tree
- Random Forrest
- Linear Descriminant Analysis
- Ada Boost Classifier
- Gradient Boosting Classifier

Initialize training 

    from sklearn.model_selection import train_test_split #for split the data
    from sklearn.metrics import accuracy_score  #for accuracy_score
    from sklearn.model_selection import KFold #for K-fold cross validation
    from sklearn.model_selection import cross_val_score #score evaluation
    from sklearn.model_selection import cross_val_predict #prediction
    from sklearn.metrics import confusion_matrix #for confusion matrix
    all_features = traindf.drop("Survived",axis=1) #copy of the traindf without Survived
    Targeted_feature = traindf["Survived"]
    X_train,X_test,y_train,y_test = train_test_split(all_features,Targeted_feature,test_size=0.3,random_state=42)
    X_train.shape,X_test.shape,y_train.shape,y_test.shape

__Logistic Regression__

    from sklearn.linear_model import LogisticRegression # Logistic Regression
    model = LogisticRegression()
    model.fit(X_train,y_train)
    prediction_lr=model.predict(X_test)
    print('--------------The Accuracy of the model----------------------------')
    print('The accuracy of the Logistic Regression is',round(accuracy_score(prediction_lr,y_test)*100,2))
    kfold = KFold(n_splits=10, random_state=22) # k=10, split the data into 10 equal parts
    result_lr=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
    print('The cross validated score for Logistic REgression is:',round(result_lr.mean()*100,2))
    y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
    sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
    plt.title('Confusion_matrix', y=1.05, size=15)

__Random Forrests__

    from sklearn.ensemble import RandomForestClassifier
    model = RandomForestClassifier(criterion='gini', n_estimators=700,
                                min_samples_split=10,min_samples_leaf=1,
                                max_features='auto',oob_score=True,
                                random_state=1,n_jobs=-1)
    model.fit(X_train,y_train)
    prediction_rm=model.predict(X_test)
    print('--------------The Accuracy of the model----------------------------')
    print('The accuracy of the Random Forest Classifier is',round(accuracy_score(prediction_rm,y_test)*100,2))
    kfold = KFold(n_splits=10, random_state=22) # k=10, split the data into 10 equal parts
    result_rm=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
    print('The cross validated score for Random Forest Classifier is:',round(result_rm.mean()*100,2))
    y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
    sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
    plt.title('Confusion_matrix', y=1.05, size=15)

__Support Vector Machines__

    from sklearn.svm import SVC, LinearSVC

    model = SVC()
    model.fit(X_train,y_train)
    prediction_svm=model.predict(X_test)
    print('--------------The Accuracy of the model----------------------------')
    print('The accuracy of the Support Vector Machines Classifier is',round(accuracy_score(prediction_svm,y_test)*100,2))
    kfold = KFold(n_splits=10, random_state=22) # k=10, split the data into 10 equal parts
    result_svm=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
    print('The cross validated score for Support Vector Machines Classifier is:',round(result_svm.mean()*100,2))
    y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
    sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
    plt.title('Confusion_matrix', y=1.05, size=15)

__KNN Classifier__

    from sklearn.neighbors import KNeighborsClassifier


    model = KNeighborsClassifier(n_neighbors = 4)
    model.fit(X_train,y_train)
    prediction_knn=model.predict(X_test)
    print('--------------The Accuracy of the model----------------------------')
    print('The accuracy of the K Nearst Neighbors Classifier is',round(accuracy_score(prediction_knn,y_test)*100,2))
    kfold = KFold(n_splits=10, random_state=22) # k=10, split the data into 10 equal parts
    result_knn=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
    print('The cross validated score for K Nearest Neighbors Classifier is:',round(result_knn.mean()*100,2))
    y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
    sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
    plt.title('Confusion_matrix', y=1.05, size=15)

__Gaussian Naive Bayes__

    from sklearn.naive_bayes import GaussianNB
    model= GaussianNB()
    model.fit(X_train,y_train)
    prediction_gnb=model.predict(X_test)
    print('--------------The Accuracy of the model----------------------------')
    print('The accuracy of the Gaussian Naive Bayes Classifier is',round(accuracy_score(prediction_gnb,y_test)*100,2))
    kfold = KFold(n_splits=10, random_state=22) # k=10, split the data into 10 equal parts
    result_gnb=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
    print('The cross validated score for Gaussian Naive Bayes classifier is:',round(result_gnb.mean()*100,2))
    y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
    sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
    plt.title('Confusion_matrix', y=1.05, size=15)

__Decision Tree__

    from sklearn.tree import DecisionTreeClassifier
    model= DecisionTreeClassifier(criterion='gini', min_samples_split=10,min_samples_leaf=1, max_features='auto')
    model.fit(X_train,y_train)
    prediction_tree=model.predict(X_test)
    print('--------------The Accuracy of the model----------------------------')
    print('The accuracy of the DecisionTree Classifier is',round(accuracy_score(prediction_tree,y_test)*100,2))
    kfold = KFold(n_splits=10, random_state=22) # k=10, split the data into 10 equal parts
    result_tree=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
    print('The cross validated score for Decision Tree classifier is:',round(result_tree.mean()*100,2))
    y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
    sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
    plt.title('Confusion_matrix', y=1.05, size=15)

__AdaBoost__

    from sklearn.ensemble import AdaBoostClassifier
    model= AdaBoostClassifier()
    model.fit(X_train,y_train)
    prediction_adb=model.predict(X_test)
    print('--------------The Accuracy of the model----------------------------')
    print('The accuracy of the AdaBoostClassifier is',round(accuracy_score(prediction_adb,y_test)*100,2))
    kfold = KFold(n_splits=10, random_state=22) # k=10, split the data into 10 equal parts
    result_adb=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
    print('The cross validated score for AdaBoostClassifier is:',round(result_adb.mean()*100,2))
    y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
    sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
    plt.title('Confusion_matrix', y=1.05, size=15)

__Linear Descriminant Analysis__

    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    model= LinearDiscriminantAnalysis()
    model.fit(X_train,y_train)
    prediction_lda=model.predict(X_test)
    print('--------------The Accuracy of the model----------------------------')
    print('The accuracy of the LinearDiscriminantAnalysis is',round(accuracy_score(prediction_lda,y_test)*100,2))
    kfold = KFold(n_splits=10, random_state=22) # k=10, split the data into 10 equal parts
    result_lda=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
    print('The cross validated score for AdaBoostClassifier is:',round(result_lda.mean()*100,2))
    y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
    sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
    plt.title('Confusion_matrix', y=1.05, size=15)

__Gradient Boosting Classifier__

    from sklearn.ensemble import GradientBoostingClassifier
    model= GradientBoostingClassifier()
    model.fit(X_train,y_train)
    prediction_gbc=model.predict(X_test)
    print('--------------The Accuracy of the model----------------------------')
    print('The accuracy of the Gradient Boosting Classifier is',round(accuracy_score(prediction_gbc,y_test)*100,2))
    kfold = KFold(n_splits=10, random_state=22) # k=10, split the data into 10 equal parts
    result_gbc=cross_val_score(model,all_features,Targeted_feature,cv=10,scoring='accuracy')
    print('The cross validated score for AdaBoostClassifier is:',round(result_gbc.mean()*100,2))
    y_pred = cross_val_predict(model,all_features,Targeted_feature,cv=10)
    sns.heatmap(confusion_matrix(Targeted_feature,y_pred),annot=True,fmt='3.0f',cmap="summer")
    plt.title('Confusion_matrix', y=1.05, size=15)

### Model Evaluation

Quick dataframe ranking all the models we tested:

    models = pd.DataFrame({
        'Model': ['Support Vector Machines', 'KNN', 'Logistic Regression', 
                'Random Forest', 'Naive Bayes', 'AdaBoostClassifier', 
                'Gradient Decent', 'Linear Discriminant Analysis', 
                'Decision Tree'],
        'Score': [result_svm.mean(), result_knn.mean(), result_lr.mean(), 
                result_rm.mean(), result_gnb.mean(), result_adb.mean(), 
                result_gbc.mean(), result_lda.mean(), result_tree.mean()]})
    models.sort_values(by='Score',ascending=False)




---


## Titanic Classifier

- demo project - run off of the given code. 
    - random forest model
- __Result: 77%__
- tuning forest model:
    - trees from 100 to 150
    - max_depth from 5 to 6
    - add more features to the model
        - NaN error - got to clean the data first

## Digit Classifier

- data is loaded in with pd.read_csv. Use .head to show some data

## Advanced Regressions with Housing Dataset

- load data
- drop columns with <50% values
- correlation matrix - set xticklabels and yticklabels=True 
