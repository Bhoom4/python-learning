# program using function to remove a given word from a list and strip it at the same Time

def remove(l,word):
    for i in l:
        l.remove(word)
        return l

l=["bhoom","bhoomika","dev",56,8,"heyyy"]
g=remove(l,"bhoom")
print(g)

#strip
def remove(l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l=["bhoom","bhoomika","dev","heyyy"]
g=remove(l,"bhoom")
print(g)