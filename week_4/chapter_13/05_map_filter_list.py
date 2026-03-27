# Map 
from functools import reduce
l=[1,2,3,4]
square=lambda x:x*x

squarelist = map(square,l)
print(list(squarelist))  #it should be in list so u have to add list


# Filter
def even(n):
    if(n%2 == 0):
        return True 
    return False

Even = filter(even,l)
print(list(Even))

# Reduce            # you have import the reduce funtion
def sum(a,b):
    return a+b

mul =lambda x,y:x*y
print(reduce(sum,l))
print(reduce(mul,l))

    