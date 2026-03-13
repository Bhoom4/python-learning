

with open ("week_3/chapter_9_practice/log.txt","r")as f:
    l=f.readlines()

lineno=1
for line in l:
    if("python" in line):
        print(f"yes the word python exist in line:{lineno}")
        break
    line += 1
else:
    print("no not present")
    