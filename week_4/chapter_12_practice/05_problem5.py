n=int(input("enter a number: "))

table=[n*i for i in range(1,11)]
with open ("week_4/chapter_12_practice/05_table.txt","a") as f:
    f.write(f"table of {n} : {str(table)} \n")