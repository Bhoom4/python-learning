with open ("week_3/chapter_9_practice/log.txt","r")as f:
    c=f.read()

if("python" in c):
    print("yes the word python exist")
else:
    print("no")