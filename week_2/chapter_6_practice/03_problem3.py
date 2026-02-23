p1="make a lot"
p2="buy now"
p3="subscribe this"
p4="click here"

m = input("enter your message:")

if(p1 in m or p2 in m or p3 in m or p4 in m):
    print("this message is a spam")
else:
    print("this is not a spam")