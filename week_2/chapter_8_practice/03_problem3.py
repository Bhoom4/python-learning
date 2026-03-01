# write a recursive function to calculate the sum of firdt 'n' natural number

def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
n =int(input("enter the value of n: "))
print(sum(n))
    