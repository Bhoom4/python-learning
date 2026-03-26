a= int(input("enter a number: "))
b= int(input("enter a second number: "))

if(b==0):
    raise ZeroDivisionError("we dont divide any number by zero")
else:
    print(f"the division a/b is {a/b}")