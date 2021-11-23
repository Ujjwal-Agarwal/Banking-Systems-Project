import mysql.connector as mysql
from Crypto.Cipher import AES
import base64,random,string,os, base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


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

def Key_enc_key(passw):
    password = passw.encode()

    salt = b"\xb9\x1f|}'S\xa1\x96\xeb\x154\x04\x88\xf3\xdf\x05"

    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),
                length=24,
                salt=salt,
                iterations=100000,
                backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key
    
    #print(key)

def msg_pad(msg):
    while len(msg)%16 !=0:
        msg = msg +' '
    return msg

def to_bytes(s):
    if type(s) is bytes:
        return s
    elif type(s) is str or (sys.version_info[0] < 3 and type(s) is unicode):
        return s.encode('utf-8')
    else:
        raise TypeError("Expected bytes or string, but got %s." % type(s))       
    

def AES_ENCRYPT(data,key):
    #key = key.encode('utf-8')
    iv = os.urandom(16)
    #iv = iv.encode('utf-8')
    print(len(key))
    cipher = AES.new(key,AES.MODE_CBC,iv)
    msg = msg_pad(data)
    msg = to_bytes(msg)


    enc = cipher.encrypt(msg)
    return enc
    



def AES_DECRYPT(encd,key,iv):
    aes = AES.new(key, AES.MODE_CBC, iv)
    decd = adec.decrypt(encd)
    return decd





def Insert_Customer_Entry():
    name = input("Insert Customer Name\n")
    Phone = input("Insert Customer Phone Number\n")
    Email = input("Insert Customer Email\n")
    Date_Of_Birth = input("Insert Customer DOB\n")
    #formatted_date = Date_Of_Birth.strftime('%Y-%m-%d %H:%M:%S')
    Pass = input("Insert USER PASSWORD\n") #PASSWORD WOULD ONLY BE SAVED BY THE CUSTOMER
    Conf_Pass = input("Confirm USer Password\n")


    #PASSWORD CONFIRMATION
    if Pass != Conf_Pass:
        print("Password Does Not Match!")
        while Pass != Conf_Pass:
            Pass = input("Insert USER PASSWORD\n")
            Conf_Pass = input("Confirm USer Password\n")
    
    

    # File Encryption Key
    key = ''.join(random.choices(string.ascii_letters+string.digits,k=32))
    print(key)

    #Generating Key Encryption Key KEK
    kekkey = Key_enc_key(Pass)
    print("keklen"+str(len(kekkey)))
    #key = AES_ENCRYPT(key,kekkey)


    #QUERY, using MYSQL AES_ENCRYPT FUNCTION TO ENCRYPT THE DATA USING THE FEK
    query  = "INSERT INTO CUSTOMER VALUES(%s,aes_encrypt(%s,%s),aes_encrypt(%s,%s),aes_encrypt(%s,%s),%s,%s)"
    
    #VALUE DEF.
    values = (seqgen,name,key,Phone,key,Email,key,Date_Of_Birth,key)
    #values = ("NULL","Ujjwal","737393","sdsdwds",'2017-07-08',"12345","va")

    #print(name,Phone,Email,Date_Of_Birth,Pass,Customer_type)
    
    #CURSOR EXECUTION
    cursor.execute(query,values)

    db.commit()

#Insert_Customer_Entry()


    

