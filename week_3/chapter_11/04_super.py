class emp:
    def __init__(self):
        print("constructor of emp")
    a=1

class manager(emp):
    def __init__(self):
        super().__init__()    #it runs the constructor of emp also
        print("constructor of manager")
    b=2

class coder(manager):
    def __init__(self):
        super().__init__()
        print("constructor of coder")
    c=3

o=emp()
print(o.a)

o=manager()
print(o.a,o.b)


o=coder()
print(o.a,o.b,o.c)