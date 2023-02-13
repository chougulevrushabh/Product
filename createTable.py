import mysql.connector

import os
from dotenv import load_dotenv
load_dotenv()


LOCALHOST = os.environ.get("host")
print("LOCALHOST", LOCALHOST)
USER_NAME = os.environ.get("user")
PASSWORD = os.environ.get("password")
DATABASE = os.environ.get("database")

myDatabase = mysql.connector.connect(host=LOCALHOST, user=USER_NAME,  password=PASSWORD,  database=DATABASE

                           )
if myDatabase.is_connected():

    myCursor = myDatabase.cursor()
    # # myCursor.execute("CREATE DATABASE Products")

    # This code is used to show tables in the database.
    # myCursor.execute("SHOW TABLES")  
    # for x in myCursor:
    #     print(x)          # This code is used to show tables in the database.

   
    myCursor.execute(
        "CREATE TABLE products (id varchar(50) , shape varchar(50), size varchar(50), location varchar(50),price varchar(50))")
    myCursor.execute(
        "CREATE TABLE user (name varchar(50) , age varchar(50), address varchar(50))")
    myCursor.execute(
        "CREATE TABLE Recommendation (id varchar(50) , product_id  varchar(50), user_id varchar(50))")
