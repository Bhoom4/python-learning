'''f = open("week_3/chapter_9/file.txt")
   d=f.read()
   print(d)
   f.close()''' # instead of writing all this u can use "with" statement

with open("week_3/chapter_9/file.txt") as f:
    print(f.read()) 
    # no closing is needed