class Emp:
    name="bhoomika"
    age=21
    sal=100000

b = Emp()
print(b.name,b.age)


#2
class Emp:     #class
    age=21            # class attribute
    sal=100000

bhoomika = Emp() #object
bhoomika.name="bhoomika" #object attribute
print(bhoomika.name,bhoomika.age,bhoomika.sal)

dev = Emp()
dev.name="dev"
print(dev.name,dev.age,dev.sal)
#here name is obj attribute 
#sal and age belong directly to class attribute so they are class attribute