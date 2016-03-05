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
        p.append(associations.index(x))
    #print(p)
    K=[]
    for x in key:
        K.append(associations.index(x))
    c=[]
    while z<len(p):
        c.append((p[z]+K[z%len(K)])%len(associations))
        z=z+1
    #print(c)
    z=0
    C=[]
    while z<len(c):
        C.append(associations[c[z]])
        z=z+1
    #print(C)
    a=""
    for x in C:
        a=a+x
    print(a)
    return(a)


def decrypt(C):
    key=str(input("What is your key"))
    C=list(C)
    c=[]
    for x in C:
        c.append(associations.index(x))
    K=[]
    for x in key:
        K.append(associations.index(x))
    
    z=0
    p=[]
    while z<len(c):
        p.append((c[z]+K[z%len(K)])%len(associations))
        z=z+1
    
    print(p)
    
    
def requesting_ans():
    req=input("Enter e to encrypt, d to decrypt, q to quit")
    if req=="e":
        mess=str(input("message to encrypt"))
        encrypt(mess)
    elif req=="d":
        mess=str(input("message to decrypt"))
        decrypt(mess)
    elif req=="q":
        print("Goodbye")
        return()
    else:
        print("Sorry did not understand")
        requesting_ans()
        
requesting_ans()