import mysql.connector as mysql
from pyotp import totp
from Insertion import AES_ENCRYPT,AES_DECRYPT, Key_enc_key
import os, pyotp,base64

#SQL connection to use the required database
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "pydbtest"
)

#Cursor initialized to use the current connection
cursor = db.cursor()

def Authentication():
    Account_Name = input("ENTER ACCOUNT NAME: ")
    Cust_ID = str(input("ENTER CUSTOMER ID: "))
    Pass = input("ENTER PASSWORD: ")

    query = "SELECT USER_PASSWORD FROM CUSTOMER WHERE CUSTOMER_ID= " + Cust_ID
    cursor.execute(query)
    encFEK = cursor.fetchone()
    encFEK = encFEK[0]

    KEK = Key_enc_key(Pass)

    FEK = AES_DECRYPT(encFEK,KEK)
    FEK = FEK.decode()

    query = "SELECT CAST(AES_DECRYPT(ACCOUNT_NAME," +"'" + FEK + "'"+ ") AS CHAR) FROM ACCOUNT WHERE CUSTOMER_ID = " + Cust_ID
    cursor.execute(query)
    Acc_Name_Auth = cursor.fetchone()
    Acc_Name_Auth = Acc_Name_Auth[0]
    print(Acc_Name_Auth)

    if(Acc_Name_Auth!= Account_Name):
        #os.system('cls' if os.name == 'nt' else 'clear')
        print("WRONG ACCOUNT!")
        quit()

    '''OTP System'''

    query = "SELECT CAST(AES_DECRYPT(TOTP_KEY,"+ "'" + FEK + "'" +") AS CHAR) FROM AUTH WHERE CUSTOMER_ID = " + Cust_ID
    cursor.execute(query)
    TOTP_KEY = cursor.fetchone()
    TOTP_KEY = TOTP_KEY[0]

    totp = pyotp.TOTP(base64.b32encode(bytearray(TOTP_KEY,'ascii')).decode('utf-8'))
    
    TOTP_VERIFY = input("ENTER THE KEY FROM YOUR AUTHENTICATOR APP :")
    
    if totp.verify(TOTP_VERIFY) !=True:
        print("WRONG AUTHENTICATION KEY!")
        quit()
    

    print("AUTHENTICATION SUCCESS!")
    return True


    '''query = "SELECT CAST(AES_DECRYPT(EMAIL," +"'" + FEK + "'"+ ") AS CHAR) FROM CUSTOMER WHERE CUSTOMER_ID = " + Cust_ID
    cursor.execute(query)
    EMAIL2 = cursor.fetchone()
    print(EMAIL2)'''

Authentication()




