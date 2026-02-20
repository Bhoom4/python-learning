#union
a = {"harruy",6,4,9,56,"gev"}
b = {"lksh","gev",7,8,9}

print(a.union(b))

#intersection
a = {"harruy",6,4,9,56,"gev"}
b = {"lksh","gev",7,8,9}
print(a.intersection(b)) 

c={7,8}.issubset(a)
print(c)
print({7,8}.issubset(b))

print(a.issuperset({"gev"}))
