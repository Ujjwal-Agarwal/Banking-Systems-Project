import mysql.connector as mysql
from Insertion import AES_ENCRYPT,AES_DECRYPT, Key_enc_key

#SQL connection to use the required database
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pydbtest"
)

#Cursor initialized to use the current connection
cursor = db.cursor()

def Transaction():
    Account_Name = input("ENTER ACCOUNT NAME: ")
    Cust_ID = str(input("ENTER CUSTOMER ID: "))
    Pass = input("ENTER PASSWORD: ")

    query = "SELECT USER_PASSWORD FROM CUSTOMER WHERE CUSTOMER_ID= " + Cust_ID
    cursor.execute(query)
    encFEK = cursor.fetchone()
    print(encFEK)
    encFEK = encFEK[0]
    print(encFEK)

    KEK = Key_enc_key(Pass)
    print("KEK")
    print(KEK)

    FEK = AES_DECRYPT(encFEK,KEK)
    FEK = FEK.decode()
    print("FEK")
    print(FEK)

    query = "SELECT EMAIL FROM CUSTOMER WHERE CUSTOMER_ID = " + Cust_ID
    cursor.execute(query)
    EMAIL = cursor.fetchone()
    print("ENCRYPTED EMAIL")
    print(EMAIL)
    query = "SELECT CAST(AES_DECRYPT(EMAIL," +"'" + FEK + "'"+ ") AS CHAR) FROM CUSTOMER WHERE CUSTOMER_ID = " + Cust_ID
    cursor.execute(query)
    EMAIL2 = cursor.fetchone()
    print("EMAIL")
    print(EMAIL2)





Transaction()

