import pyotp,base64

TOTP_KEY = input("ENTER YOUR 2FA PASSWORD: ")
totp = pyotp.TOTP(base64.b32encode(bytearray(TOTP_KEY,'ascii')).decode('utf-8'))

print(totp.now())
