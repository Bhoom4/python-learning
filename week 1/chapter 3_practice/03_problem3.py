# write a pg to detect a double space

#1
a = "bhoomika is reading a book rn"
print(a.find("  ")) #here it will retuen -1 as output bcs it detected no double space

#2
a = "bhoomika is reading a  book rn"
print(a.find("  ")) # here it gives the correct o/p
