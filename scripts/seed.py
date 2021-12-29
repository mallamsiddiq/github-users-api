import mysql.connector
import pandas as pd
import requests
import json


total=int(input("total"))

d=requests.get('https://api.github.com/users').json()
df = pd.DataFrame.from_records(d)

data=df[['id','login','url','avatar_url','type','html_url']]
data2=data.to_json(orient='records')
data2=json.loads(data2)


'''#mycursor.execute("CREATE DATABASE github_users_database")

mydb = mysql.connector.connect(
  host="localhost",
  user="nutfa",
  password="radunni",
  database="github_users_database"
)

mycursor = mydb.cursor()



#mycursor.execute("CREATE TABLE github_users( id VARCHAR(255), name VARCHAR(255),url VARCHAR(255), avatar_url VARCHAR(255), type VARCHAR(255))")

mycursor.executemany("""
    INSERT INTO blog_github_users (id, name, url, avatar_url,type,date_created,html_url)
    VALUES (%(id)s, %(login)s,%(url)s, %(avatar_url)s, %(type)s ,'2014-04-02 08:49:43',%(html_url)s)""", data2)

mydb.commit() '''

print (data2)