w = ["good","bad","day","table"]

with open("week_3/chapter_9_practice/file.txt","r") as f:
    c = f.read()

for w in w:
    c =c.replace(w,"#"* len(w))

with open("week_3/chapter_9_practice/file.txt","w") as f:
    c = f.write(c)

