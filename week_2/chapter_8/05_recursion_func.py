'''facrorial(0)=1
fact(1)=1
fact(2)=2x1
fact(3)=3x2x1
.
.
factorial(n)=n*factorial(n-1)'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n* factorial(n-1)
n=int(input("enter a number:"))
print("the factorial of a number is:",factorial(n))
# print(f"the factorial of a number is:{factorial(n)}")