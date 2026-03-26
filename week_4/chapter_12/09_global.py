
a=45  # this is a global 'a'
def fun():
    global a   #doing this will change the a=45 to 7
    a=7
    print(a)
    

fun()
print(a)
