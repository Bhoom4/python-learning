#  pg to convert fahrenhet to celcius

def f_to_c(f):
    return 5*(f-32)/9

f=int(input("enter a temreature in f: "))
h=f_to_c(f)
print(f"temperature in f: {round(h,2)} ° c ") # round() funtion is used to round of dec to whole number i.e 37.7777777778=37.78