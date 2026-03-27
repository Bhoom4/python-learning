try:
    a=int(input("enter a: "))
    b=int(input("enter b: "))
    print(a/b)
except ZeroDivisionError as z:
    print("do not support num divsible by 0")
     