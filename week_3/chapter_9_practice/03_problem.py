def generateTable(n):
    table = ""
    for a in range(1,11):
        table += f"{n}*{a}={n*a}\n"

    with open(f"week_3/chapter_9_practice/tables/table_{n}.txt","w")as f:
        f.write(table)

for  a in range(2,21):
    generateTable(a)