# what will happen if the names of the two friends are same from problem 6?

d = {}
name=input("enter your name:")
lang=input("enter your fav language:")
d.update({name:lang})
name=input("enter your name:")
lang=input("enter your fav language:")
d.update({name:lang})
name=input("enter your name:")
lang=input("enter your fav language:")
d.update({name:lang})
name=input("enter your name:")
lang=input("enter your fav language:")
d.update({name:lang})
print(d)

#ans: it will update the newer value for the same name.

# and if suppose the values are same then it will print both same values,so the value can be same but key shoudnt be same.