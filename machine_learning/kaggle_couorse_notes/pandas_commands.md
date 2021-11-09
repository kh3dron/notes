### Viewing Data

frame.describe()
frame.val_contents()
frame.hist()
frame.dead()

### Processing

frame.isnull().sum()   
frame.select_dtypes(exclude=['object']) #drop cols of a type

replace all nulls with mode:

    for e in frame.columns:
        frame[e].fillna(train_df[e].mode()[0], inplace = True)

### Creating Frames

- pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
- index constructor: rows are indexes
  - pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Product A', 'Product B'])
- a series is a single column of a df
- reading data frames from csv
  - pd.read_csv("file")
    - file, index_col=0
- pd.shape()
  - (rows, cols) (indexes, series)
- pd.head
  - first 5 indexes

### Indexing, Selecting & Assigning

- frame[column]
- frame[column][row]
- frame.iloc[0] to grab first row
- frame.iloc[:, 0] to grab 0th column
- frame.iloc[:3, 0] for first 3 0th column values
- generally list rules apply
  - frame.iloc[1:5, -1] and all that
- grab some columns:
  - frame.iloc[0, [col1, col2, col3]]
- frame.set_index(name)
- conditional selection
  - col == name
  - frame.loc[frame.column == value]
  - reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)]
  - reviews.loc[reviews.country.isin(['Italy', 'France'])]
  - reviews.loc[reviews.price.notnull()]
- assigning data
  - reviews['critic'] = 'everyone'
  - reviews['index_backwards'] = range(len(reviews), 0, -1)
  - top_oceania_wines = reviews[reviews.country.isin(["Australia", "New Zealand"]) & (reviews.points>=95)]

### Summary Functions and Maps

- frame.column.describe()
- frame.col.mean()
- reviews.taster_name.unique()
- reviews.taster_name.value_counts()
- maps
  - review_points_mean = reviews.points.mean()
  - reviews.points.map(lambda p: p - review_points_mean)
- apply a function to a row

    def remean_points(row):
        row.points = row.points - review_points_mean
        return row

    reviews.apply(remean_points, axis='columns')

    # examaple 2

    def stars(row):
    if row.country == 'Canada' or row.points >= 95:
        return 3
    elif row.points >= 85: 
        return 2
    else:
        return 1

    star_ratings = reviews.apply(stars, axis='columns')



- apply and new do NOT modify frames in place, they return new frames
- built in mapping operations:

    review_points_mean = reviews.points.mean()
    reviews.points - review_points_mean

    reviews.country + " - " + reviews.region_1

- idxmax

    bargain_idx = (reviews.points / reviews.price).idxmax()
    bargain_wine = reviews.loc[bargain_idx, 'title']

- count the occurance of a word

    n_trop = reviews.description.map(lambda desc: "tropical" in desc).sum()
    n_fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
    descriptor_counts = pd.Series([n_trop, n_fruity], index=['tropical', 'fruity'])

### Grouping and Sorting

- groupwise analysis
  - reviews.groupby('points').points.count()
  - reviews.groupby('points').price.min()