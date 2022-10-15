from cryptography.fernet import Fernet



file=open('key.key','rb')
key = file.read()
file.close()
f = Fernet(key)




while True:
    Select=input('What Do You Want To Do-').lower()

    if Select == 'encrypt':
       en = input("Type Text To Encrypt:")
       msg = bytes(en, 'utf-8')
       pw = f.encrypt(msg)
       out = str(pw,'utf-8')
       print("Encrypted Text-",out)
    elif Select == 'decrypt':
       en = input("Type Text To decrypt:")
       msg = bytes(en, 'utf-8')
       pw = f.decrypt(msg)
       out = str(pw,'utf-8')
       print("Encrypted Text-",out)
    else:
       print('Unknown Command') 