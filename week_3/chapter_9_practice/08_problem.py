with open("week_3/chapter_9_practice/this.txt","r") as f:
    c=f.read()

with open("week_3/chapter_9_practice/this_copy.txt","w") as f:
    f.write(c)