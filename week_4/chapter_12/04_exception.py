try:
    a= int(input("enter  a number: "))
    print(a)

except ValueError as v:
    print("hhhhhh")
    print(v)

except Exception as e:   # all other type of exceptions are handled here
    print(e)

print("hey there")