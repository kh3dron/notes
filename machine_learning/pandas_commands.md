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

