marks = int(input("enter your marks: "))

if(marks<=100 and marks>90):
     grade="ex"
elif(marks<=90 and marks>80):
     grade="A"
elif(marks<=80 and marks>70):
     grade="b"
elif(marks<=70 and marks>60):
     grad="c"
elif(marks<=60 and marks>50):
     grade="f"
print("your grade is:",grade)