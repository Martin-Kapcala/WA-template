from datetime import date
class User:
    
    
    def __init__(self,nick,email, datumReg):
        self.__email = email
        self.__datumReg = datumReg
        self.__nick = nick

    def __init__(self, nick):
        self.__nick = nick
        self.__email = "nezadán"
        self.__datumReg = date.today()

    def get_nick(self):
        return self.__nick
    
    def set_nick(self,nick):
        self.__nick = nick

    def get_datum_registrace(self):
        return self.__datumReg
    
    def get_email(self):
        return self.__email

    def toString(self):
        return (f"<p><b>User:</b> {self.get_nick()}</br><b>e-mail:</b> {self.__email}\n</br><b>Datum registrace:</b> {self.__datumReg}</p>")
    
    from flask import Flask

        

