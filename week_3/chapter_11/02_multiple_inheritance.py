class emp:
    name="bh"
    company="GHY"
    def show(self):
        print(f"the name of the emp is: {self.name} and the company is {self.company}")

class coder:
    lang="py" 
    def plang(self):
        print(f"the language is: {self.lang}")

class programmer(emp,coder):
    company="GHYtech"
    def showlang(self):
        print(f"the name is {self.name} and he is good with {self.lang}")  

a=emp()
b=programmer() 

b.show()
b.plang()
b.showlang()


