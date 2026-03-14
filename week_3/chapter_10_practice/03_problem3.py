'''Create a class with a class attribute a; create an object from it and set 'a' directly using object.a = o. 
Does this change the class attribute? '''

class aaa:
    a=4

object=aaa()  
print(object.a) #prints the class attribute

object.a=0    #instance attribute
print(object.a)   #prints the instance attribute because instane attribute is present
print(aaa.a)