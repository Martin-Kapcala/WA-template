class User:
    nick = ""
    email = ""
    datumReg = ""

    def __init__(self,nick,email, datumReg):
        self.email = email
        self.datumReg = datumReg
        self.nick = nick
    
    def toString(self):
        return (f"User: {self.nick}\ne-mail: {self.email}\nDatum registrace: {self.datumReg}")
        

