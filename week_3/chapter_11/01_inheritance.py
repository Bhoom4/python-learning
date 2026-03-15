class emp:
    company="GHY"
    def show(self):
        print(f"the name of the emp is: {self.name} and the sal is {self.sal}")

class programmer(emp):
    company="GHYtech"
    def showlang(self):
        print(f"the name id {self.name} and he is good with {self.language}")  

a=emp()
b=programmer() 
print(a.company,b.company)   
