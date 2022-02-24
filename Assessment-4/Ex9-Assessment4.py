import requests
import pandas as pd
import json

myobj = {
    "userId": 1,
    "title": "delectus aut autem",
    "completed": "false"
}
url = 'https://jsonplaceholder.typicode.com/todos/1'
x=requests.post(url,data = myobj)
r=requests.delete(url,data = myobj )
print(r.status_code) #To print status code after deleted the data