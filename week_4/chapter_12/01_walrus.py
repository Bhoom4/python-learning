#without walrus operator
n = len([1,2,3,4,5])
if(n > 3):
    print(f"list is too long ({n} elements, expected<=3)")


# with walrus operator
if(n := len([1,2,3,4,5]))> 3:
    print(f"list is too long ({n} elements, expected<=3)")

