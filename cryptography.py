"""
cryptography.py
Author: Ethan Adner
Credit: 

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
associations=list(associations)


def encrypt():
    print()
def decrypt():
    print()
def requesting_ans():
    req=input("Enter e to encrypt, d to decrypt, q to quit")
    if req=="e":
        mess=str("message to encrypt")
        encrypt(mess)
    elif req=="d":
        mess=str(input("message to decrypt"))
        decrypt()
    elif req=="q":
        return("Goodbvye")
    else:
        print("Sorry did not understand")
        requesting_ans()
        
requesting_ans()