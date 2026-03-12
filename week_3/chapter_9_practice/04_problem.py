w = "good"

with open("week_3/chapter_9_practice/file.txt","r") as f:
    c = f.read()

cnew=c.replace(w,"#####")

with open("week_3/chapter_9_practice/file.txt","w") as f:
    c = f.write(cnew)

