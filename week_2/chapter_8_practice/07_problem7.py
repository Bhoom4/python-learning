# pg to print multiplication of a given number using function

def mul(n):
    for i in range(1,11):
        print(f"{n}X{i}={n*i}")
n=int(input("enter a number: ")) 
print(mul(n))