

# Samnple Workflow
From this helpful guide: https://www.kaggle.com/vinothan/titanic-model-with-90-accuracy

##### Identify Missing Data: Populate or Delete

Renders a bar chart of whic data is the most missing. 

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

##### Feature Engineering

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

- already have some chunks of a pytorch neural network - try to get that too run with the kaggle data
