import mysql.connector as mysql

#SQL connection to use the required database
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pydbtest"
)

#Cursor initialized to use the current connection
cursor = db.cursor()

#VALUE FOR AUTO INCREMENT SEQUENCING IN TABLE
seqgen = 0

def Insert_Customer_Entry():
    name = input("Insert Customer Name\n")
    Phone = input("Insert Customer Phone Number\n")
    Email = input("Insert Customer Email\n")
    Date_Of_Birth = input("Insert Customer DOB\n")
    #formatted_date = Date_Of_Birth.strftime('%Y-%m-%d %H:%M:%S')
    Pass = input("Insert USER PASSWORD\n")
    Conf_Pass = input("Confirm USer Password\n")


    #PASSWORD CONFIRMATION
    if Pass != Conf_Pass:
        print("Password Does Not Match!")
        while Pass != Conf_Pass:
            Pass = input("Insert USER PASSWORD\n")
            Conf_Pass = input("Confirm USer Password\n")
    
    Customer_type = input("Insert Customer Type")

    #QUERY
    query  = "INSERT INTO CUSTOMER(CUSTOMER_ID,CUSTOMER_NAME,PHONE_NUMBER,EMAIL,DATE_OF_BIRTH,USER_PASSWORD,CUSTOMER_TYPE) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    
    #VALUE DEF.
    values = (seqgen,name,Phone,Email,Date_Of_Birth,Pass,Customer_type)
    #values = ("NULL","Ujjwal","737393","sdsdwds",'2017-07-08',"12345","va")

    #print(name,Phone,Email,Date_Of_Birth,Pass,Customer_type)
    
    #CURSOR EXECUTION
    cursor.execute(query,values)

    db.commit()


    

