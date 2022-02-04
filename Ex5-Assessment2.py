import sqlite3  

connection = sqlite3.connect('Theatre1.db')  
cursor = connection.cursor()  
cursor.execute("CREATE TABLE Movies (Movie_name text,Year_of_release integer, Genre text, awards_won text, lead_actor text, lead_actres text)")  
connection.commit()  
print("Table created")  
cursor.execute("INSERT INTO Movies VALUES('spiderman',2022,'science fiction','Oscar','Tob','kriston')")  
connection.commit()  
cursor.execute("INSERT INTO Movies VALUES('ABC',2021,'action','flim fare award','Vijay','soni')")  
connection.commit()  
print("value is inserted")  
#cursor.execute("SELECT * FROM Movies") 
#print(cursor.fetchall()) 
connection.close()  
print("Connection closed") 

 