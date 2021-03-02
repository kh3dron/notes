import pandas as pd
import tensorflow as tf
from matplotlib import pyplot as plt

print("hello")

# Import the dataset.
training_df = pd.read_csv(filepath_or_buffer="https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv")

# Scale the label.
training_df["median_house_value"] /= 1000.0

# Print the first rows of the pandas DataFrame.
training_df.head()

# Get statistics on the dataset.
#This is dope
training_df.describe()

#correlation matrix for each column
training_df.corr()