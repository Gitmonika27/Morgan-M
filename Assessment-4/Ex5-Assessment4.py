import requests
import pandas as pd

x = requests.get('https://jsonplaceholder.typicode.com/todos')
print(x.status_code) #To print status code

df=pd.read_json('https://jsonplaceholder.typicode.com/todos')
print(df.head(5)) #To print data of 5 rows
