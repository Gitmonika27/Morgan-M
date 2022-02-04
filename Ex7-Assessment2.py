import requests 
from bs4 import BeautifulSoup as bs

URL = 'https://www.imdb.com/chart/moviemeter'
req = reqests.get(URL)
soup = bs(req.text,'html.parser')

titles = soup.findall('td',attrs={'class','titlecolumn'})

titles_list=[]

count = 0
for title in titles:
    d={}
    d['Title Number']=f'Title{count}'
    d['Title Name']=title.text
    count +=1
    titles_list.append(d)

import panda as pd
df = pd.DataFrame(data=titles_list[1:10],columns=titles_list[0])
df.to_excel('user-page-html.xlsx')