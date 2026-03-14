class Emp:
    language="python"  #class attribute
    age=21
    sal=100000

bhoomika = Emp()
bhoomika.name="bhoomika"
bhoomika.language="JS"    #instance attribute
print(bhoomika.name,bhoomika.language,bhoomika.age)

#instance attribute alwas takes over the class attribute