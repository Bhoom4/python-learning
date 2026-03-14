class Emp:
    language="python"  #class attribute
    age=21
    sal=100000

    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.sal}")
    def greet(self):
        print("good morning")

bhoomika = Emp()
bhoomika.language="JS"  
bhoomika.greet()
bhoomika.getInfo()  #it can be also written as Emp.getinfo(bhoomika)