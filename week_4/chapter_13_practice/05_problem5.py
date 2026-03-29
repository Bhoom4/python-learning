from functools import reduce 
def greater(a,b):
    if(a>b):
        return a
    return b

l = [1,2,5,6,25,20,4,15,28,45]
print(reduce(greater,l))