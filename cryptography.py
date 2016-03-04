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


def encrypt(P):
    key=input("What is the encryption key?")
    P=list(P)
    z=0
    p=[]
    for x in P:
        p.append(associations.index[x])
    print(p)
    K=[]
    for x in key:
        K.append(associations.index[x])
    c=[]
    while z<len(p):
        c.append((p[z]+K[z%len(K)]))
        z=z+1



def decrypt(C):
    print()
    
    
def requesting_ans():
    req=input("Enter e to encrypt, d to decrypt, q to quit")
    if req=="e":
        mess=str(input("message to encrypt"))
        encrypt(mess)
    elif req=="d":
        mess=str(input("message to decrypt"))
        decrypt()
    elif req=="q":
        return("Goodbye")
    else:
        print("Sorry did not understand")
        requesting_ans()
        
requesting_ans()