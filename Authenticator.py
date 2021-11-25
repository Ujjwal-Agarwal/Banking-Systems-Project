import pyotp,base64,time

TOTP_KEY = input("ENTER YOUR 2FA PASSWORD: ")
totp = pyotp.TOTP(base64.b32encode(bytearray(TOTP_KEY,'ascii')).decode('utf-8'))

print(totp.now())
k = totp.now()
i = 0
while(i<10):
    k = totp.now()
    if k != totp.now():
        print(totp.now())
        k = totp.now()
