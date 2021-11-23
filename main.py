
#Start mysql server before running the program

#main.py is just used for database setup
'''
import os

os.system('sudo mysql.server start')

'''

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

#IMPORT INSERTION FUNCTIONS
'''from Insertion import Insert_Customer_Entry'''

#IMPORT DB FILLOUT FUNCTIONS
from Fillout import Account_type_Setup

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
cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER(CUSTOMER_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,CUSTOMER_NAME VARCHAR(200) NOT NULL,PHONE_NUMBER CHAR(100),EMAIL VARCHAR(300),DATE_OF_BIRTH DATE,USER_PASSWORD MEDIUMBLOB NOT NULL ) engine = innodb default charset = latin1")

#CREATE THE ACCOUNT TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS ACCOUNT(ACCOUNT_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,ACCOUNT_NAME VARCHAR(300) NOT NULL,DATE_OF_JOINING DATE,ACCOUNT_TYPE VARCHAR(100),CUSTOMER_ID INT NOT NULL, FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID) ON DELETE NO ACTION) engine = innodb default charset = latin1")

#CREATE THE ACCOUNT_TYPE TABLE
cursor.execute("CREATE TABLE IF NOT EXISTS ACCOUNT_TYPE(ACCOUNT_TYPE CHAR(3), DESCRIPTION VARCHAR(100)) engine = innodb default charset = latin1")

#CREATE THE CUSTOMER TRANSACTION LOG
cursor.execute("CREATE TABLE IF NOT EXISTS CUSTOMER_TRANSACTION_LOG(CUSTOMER_TRANSACTION_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,DATE_OF_TRANSACTION DATE,TIME_OF_TRANSACTION VARCHAR(100),AMOUNT_MANIPULATED INT NOT NULL,BALANCE_BEFORE_TRANSACTION INT NOT NULL, BALANCE_AFTER_TRANSACTION INT NOT NULL,CUSTOMER_ID INT NOT NULL, FOREIGN KEY(CUSTOMER_ID) REFERENCES CUSTOMER(CUSTOMER_ID) ON DELETE NO ACTION) engine = innodb default charset = latin1")

#CREATE THE BANKS TRANSACTION LOG
cursor.execute("CREATE TABLE IF NOT EXISTS BANK_TRANSACTION_LOG(TRANSACTION_ID VARCHAR(100) PRIMARY KEY,DATE_OF_TRANSACTION DATE,TIME_OF_TRANSACTION VARCHAR(100),AMOUNT_MANIPULATED INT,ACCOUNT_ID INT,CUSTOMER_TRANSACTION_ID INT,TRANSACTION_TYPE VARCHAR(5),FOREIGN KEY(ACCOUNT_ID) REFERENCES ACCOUNT(ACCOUNT_ID) ON DELETE NO ACTION,FOREIGN KEY(CUSTOMER_TRANSACTION_ID) REFERENCES CUSTOMER_TRANSACTION_LOG(CUSTOMER_TRANSACTION_ID)) engine = innodb default charset = latin1")

#ACCOUNT_TYPE TABLE INITIALIZATION
Account_type_Setup()


#INSERT ENTRIES INTO THE TABLE
'''Insert_Customer_Entry()''' #USE ANOTHER PROGRAM FOR CUSTOMER INPUT/OUTPUT




db.commit()