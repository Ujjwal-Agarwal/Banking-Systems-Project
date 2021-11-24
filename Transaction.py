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
    

    if(Acc_Name_Auth!= Account_Name):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("WRONG ACCOUNT!")
        quit()

    '''OTP System'''

    query = "SELECT CAST(AES_DECRYPT(TOTP_KEY," + "'" + FEK + "'" +") AS CHAR) FROM AUTH WHERE CUSTOMER_ID = " + Cust_ID
    cursor.execute(query)
    TOTP_KEY = cursor.fetchone()
    TOTP_KEY = TOTP_KEY[0]

    totp = pyotp.TOTP(base64.b32encode(bytearray(TOTP_KEY,'ascii')).decode('utf-8'))
    
    TOTP_VERIFY = input("ENTER THE KEY FROM YOUR AUTHENTICATOR APP :")
    
    if totp.verify(TOTP_VERIFY) !=True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("WRONG AUTHENTICATION KEY!")
        quit()
    

    print("AUTHENTICATION SUCCESS!")
    return (True,FEK,Cust_ID)

#Authentication()

def Balance_update(chan,mode):
    (AuthStatus,FEK,Cust_ID) = Authentication()

    if AuthStatus!= True:
        print("AUTHENTICATION FAILURE")
        quit()

    query = "SELECT CAST(AES_DECRYPT(BALANCE,"+ "'" + FEK + "'" +")AS CHAR) FROM ACCOUNT WHERE CUSTOMER_ID = " + Cust_ID
    cursor.execute(query)
    BALANCE = cursor.fetchone()
    BALANCE = BALANCE[0]
    print("INITIAL BALANACE: "+BALANCE)
    BALANCE = int(BALANCE)

    if mode == 'W':
        BALANCE = BALANCE - chan
        print("DEDUCTED AMOUNT: "+str(chan))
    elif mode == "D":
        BALANCE = BALANCE + chan
        print("ADDED AMOUNT: "+str(chan))
    
    
    print("UPDATED BALANCE IS: "+ str(BALANCE))

    query1 = "UPDATE ACCOUNT SET BALANCE = aes_encrypt(%s,%s) WHERE CUSTOMER_ID = " +Cust_ID
    values1 = (str(BALANCE),FEK)

    cursor.execute(query1,values1)
    db.commit()

Balance_update(2000,'W')