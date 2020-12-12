import pyAesCrypt
import os

class Encrypt():
    def __init__(self):
        self.bufferSize = 64 * 1024

    def encryptdata(self,userName,userPassword):
        pyAesCrypt.encryptFile(userName+".db",userName+".db.crypt",userPassword,self.bufferSize)
    
    def decryptdata(self,userName,userPassword):
        pyAesCrypt.decryptFile(userName+".db.crypt",userName+".db",userPassword,self.bufferSize)


