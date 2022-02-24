import requests
import pandas as pd
import json

myobj = {
    "userId": 10,
    "title": "macaroni",
    "completed": "false"
}
url = 'https://jsonplaceholder.typicode.com/todos/'
x=requests.post(url,data = myobj)
print(x.status_code) # To print status code,after adding above dictionary

z=(requests.get('https://jsonplaceholder.typicode.com/todos/200')) #By using get method to pull data with id 200
print(z.text)