#program to find factorial of a number using for loop
# 5!=1 x 2 x 3 x 4 x 5
n = int(input('enter a number: '))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print(f"factorial of {n} is {factorial}")