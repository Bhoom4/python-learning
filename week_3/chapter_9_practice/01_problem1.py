#pg to read a txt from a file "poem.txt" and find if the word "twinle is present in it"

f=open("week_3/chapter_9_practice/poem.txt")
d=f.read()
if("twinkle" in d):
    print("yes word twinkle is present in d")
else:
    print("no the word twinkle is not present in d")
f.close()