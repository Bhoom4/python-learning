f = open("week_3/chapter_9/file.txt")

#to read multiple lines at once
l=f.readlines()
print(l,type(l))

#to read line one by one
l1=f.readline()
print(l1,type(l1))

l2=f.readline()
print(l2,type(l2))

l3=f.readline()
print(l3,type(l3))

f.close()

#using while loop
l=f.readline()
while (l!=""):
    print(l)
    l=f.readline()
f.close()



