class programmer:
    company="microsoft"
    
    def __init__(self,name,age,sal,pin):
        self.name=name
        self.age=age
        self.sal=sal
        self.pin=pin

c=programmer("bhoomika",21,123000,23451)
print(c.name,c.age,c.sal,c.pin)

j=programmer("json",22,23455,7647)
print(j.name,j.age,j.sal,j.pin)
