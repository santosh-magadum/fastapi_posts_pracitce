from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated='auto')


def hash(password:str):
    return pwd_context.hash(password)


"""
Theory about hashing
Hashing is a one way function (well, a mapping). It's irreversible, you apply the 
secure hash algorithm and you cannot get the original string back. 

Encrypting is a proper (two way) function. It's reversible, you can decrypt the mangled string to get 
original string if you have the key.

The unsafe functionality it's referring to is that if you encrypt the passwords, your application has the key stored 
somewhere and an attacker who gets access to your database (and/or code) 
can get the original passwords by getting both the key and the encrypted text, whereas with a hash it's impossible.


You can attack a secure hash by the use of a rainbow table, which you can counteract by applying a salt to the hash before storing it.



"""

## comparing the two passwords
def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

