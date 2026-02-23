#1

post="bhoomika is a good girl, bhoomika it is then"

if("bhoomika"in post):
    print("yes it is talking about bhoomika")
else:
    print("not talking")

#2

post=input("enter a post descrip: ")

if("Bhoomika".lower()in post.lower()): # using lower enables all cases u input
    print("yes it is talking about bhoomika")
else:
    print("not talking")