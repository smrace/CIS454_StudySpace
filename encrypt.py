from flask import Flask
from flask.ext.bcrypt import Bcrypt

def crypter(password)
    bcrypt = Bcrypt{app}
    pw_hash = bcrypt.generate_password_hash(passkey).decode(‘utf-8’)
    #line to upload pw hash to data base

def authenticator(attempted_pass)
    if bcrypt.check_password_hash(database.get.pwh, attempted_pass)
       # proceed
    else 
        #wrong password
    
