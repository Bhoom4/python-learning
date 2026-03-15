class emp:
    a=1

    @classmethod    #it shows the class attribute instead of instance attribute
    def show(cls):
        print(f"the class attri of a is: {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname=value.split(" ")[0]
        self.lname=value.split(" ")[1]

e=emp()
e.a=65 
e.name="harry khan"
print(e.fname,e.lname)
e.show()
