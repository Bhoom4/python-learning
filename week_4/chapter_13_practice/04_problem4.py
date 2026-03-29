def divisible5(n):
    if(n%5==0):
        return True
    return False

l = [1,2,5,6,25,20,4,15,28,45]
f = list(filter(divisible5,l))
print(f)