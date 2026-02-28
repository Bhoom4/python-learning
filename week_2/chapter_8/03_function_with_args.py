
#1
def goodday(name):
    print("good day,"+name)
goodday("bhoomika")
goodday("harsh")
goodday("yash")

#2
def goodday(name, end):
    print("good day,"+name+" "+end)
goodday("bhoomika","thanks!")
goodday("harsh","thanks!")
goodday("yash","thanks!")

#3
def goodday(name, end):
    print("good day,"+name)
    print(end)
goodday("bhoomika","thanks!")
goodday("harsh","thanks!")
goodday("yash","thank u!")

print(" ")

#4
def goodday(name, end):
    print("good day,"+name)
    print(end)
    return "done"
g=goodday("bhoomika","thanks!")
print(g)
