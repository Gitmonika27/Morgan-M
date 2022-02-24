import pandas as pd

df = pd.read_csv('nba.csv')

print("Header:")
print(df.head(5)) #To print first 5header value
print("Shape:")
print(df.shape) # To print the dimension
print("Data Type")
print(df.dtypes) # To print the datatype of the data
print("Describe method:")
print(df.describe()) #Returns description of the data
print("Median of all data")
print(df.median())
print("Median of Age:")
print(df["Age"].median())
