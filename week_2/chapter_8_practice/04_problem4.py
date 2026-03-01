'''python program using function to print first 'n' lines of the pattern
***
**
*    for n=3'''

def pattern(n):
    if(n==0):
        return
    else:
        print("*"*n)
        pattern(n-1)

n=int(input("enter n: "))
print(pattern(n))