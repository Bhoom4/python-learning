class Emp:
    language="python"  #class attribute
    age=21
    sal=100000

    def __init__(self,name,sal,language):
        self.name=name
        self.sal=sal
        self.language=language
    print("iam creating an object")

    def getInfo(self):
        print(f"the language is {self.language}. the salary is {self.sal}")

    @staticmethod
    def greet():
        print("good morning")

bhoomika = Emp("bhoom",122000,"js")
print(bhoomika.name,bhoomika.sal,bhoomika.language)  
#bhoomika.getInfo()
#bhoomika.greet()