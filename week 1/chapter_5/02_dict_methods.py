marks = {
    "Harry":56,
    "dev":100,
    "laksh":43
}

print(marks.items())
print(marks.keys())
print(marks.get("dev"))

#diffrence between these two are
print(marks.get("heyii")) #it prints none
#print(marks["shhe"]) #it returns error

print(marks.pop("dev"))
print(marks)

print(marks.update({"laksh":67}))
print(marks)
