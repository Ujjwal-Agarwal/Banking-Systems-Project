#TO include database model in c++, refer to https://www.notion.so/ujjwalagarwal/Database-Design-560d3ac728bc4661b638ede163025caa
#Start mysql server before running the program


import mysql.connector as mysql

#Initial SQL Server Connection
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
)

#Cursor Initialization
cursor = db.cursor()
#DAtabase creation if not exists
cursor.execute("CREATE DATABASE IF NOT EXISTS pydbtest")

#Second SQL connection to use the required database
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pydbtest"
)

#Cursor initialized to use the current connection
cursor = db.cursor()

#DESCRIBE THE CUSTOMER TABLE
cursor.execute("CREATE TABLE CUSTOMER(CUSTOMER_ID INT,CUSTOMER_NAME VARCHAR(20),PHONE_NUMBER INT,EMAIL VARCHAR(50),DATE_OF_BIRTH DATE,USER_PASSWORD VARCHAR(64),CUSTOMER_TYPE CHAR(10))")


