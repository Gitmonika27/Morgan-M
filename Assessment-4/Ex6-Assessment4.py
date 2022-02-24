import requests
import pandas as pd

x = requests.get('https://jsonplaceholder.typicode.com/todos')
print(x.status_code) #To print status code

df=pd.read_json('https://jsonplaceholder.typicode.com/todos')
#print(df.to_string()) #To display entire dataset
print(df.head(7)) #To print data of 7 rows
