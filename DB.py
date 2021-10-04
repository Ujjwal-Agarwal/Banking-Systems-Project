# TO include database model in c++, refer to https://www.notion.so/ujjwalagarwal/Database-Design-560d3ac728bc4661b638ede163025caa
#Start mysql server before running the program


import mysql.connector as mysql

db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = ""
)



print(db)
