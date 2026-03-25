a= int(input("enter a numbver: "))
b= int(input("enter a second numbver: "))

if(b==0):
    raise ZeroDivisionError("we dont divide any number by zero")
else:
    print(f"the division a/b is {a/b}")