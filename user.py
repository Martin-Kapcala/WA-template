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

    
    def toString(self):
        return (f"<p><b>User:</b> {self.nick}</br><b>e-mail:</b> {self.email}\n</br><b>Datum registrace:</b> {self.datumReg}</p>")
    
    from flask import Flask

        

