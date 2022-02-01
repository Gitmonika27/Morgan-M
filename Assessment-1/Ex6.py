import sqlite3  
import json 

connection = sqlite3.connect('Theatre.db')   
cursor = connection.cursor()   
cursor.execute("CREATE TABLE Movies (Movie_name text,Year_of_release integer, Genre text, awards_won text, lead_actor text, lead_actres text)")   
connection.commit()   
cursor.execute("INSERT INTO Movies VALUES('ABC',2022,'Comedy','flim fare award','John','Maya')")   
connection.commit()   
cursor.execute("INSERT INTO Movies VALUES('BC',2021,'action','flim fare award','Vijay','soni')")   
connection.commit()   

a =(cursor.execute("SELECT * FROM Movies")) 
a = (cursor.fetchall()) 

j = json.dumps(a) 
with open('Movies_data.json','w') as f: 
f.write(j) 
f.close() 
print("Movies_data.json file is created") 

connection.close() 