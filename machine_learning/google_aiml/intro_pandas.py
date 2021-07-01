import numpy as np
import pandas as pd

print("hello")

# Create and populate a 5x2 NumPy array.
my_data = np.array([[0, 3], [10, 7], [20, 9], [30, 14], [40, 15]])

# Create a Python list that holds the names of the two columns.
my_column_names = ['temperature', 'activity']

# Create a DataFrame.
my_dataframe = pd.DataFrame(data=my_data, columns=my_column_names)

# Print the entire DataFrame
print(my_dataframe)

# Create a new column named adjusted.
my_dataframe["adjusted"] = my_dataframe["activity"] + 2

# Print the entire DataFrame
print(my_dataframe)

d1 = np.array(np.random.randint(low=0, high=101, size=(4)))
d2 = np.array(np.random.randint(low=0, high=101, size=(4)))
d3 = np.array(np.random.randint(low=0, high=101, size=(4)))
dset = np.array([d1, d2, d3])
col_names = ["Eleanor", "Chidi", "Tahani", "Jason"]
frame = pd.DataFrame(data=dset, columns = col_names)

print(frame)
print(frame["Eleanor"][0])
frame["Janet"] = frame["Tahani"]+frame["Jason"]
print(frame)