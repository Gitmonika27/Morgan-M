import requests
import pandas as pd
import json


z=(requests.get('https://jsonplaceholder.typicode.com/todos/10')) #By using get method to pull data with id 200
print(z.text)
print(z.status_code)

url = 'https://jsonplaceholder.typicode.com/todos/1'
mydata = {
    "userId": 1,
    "id": 1,
    "areaname+pincode": "delectus aut autem",
    "completed": "false"
}
r=requests.put(url,data = mydata)
print(r.status_code)
print(r.text)


