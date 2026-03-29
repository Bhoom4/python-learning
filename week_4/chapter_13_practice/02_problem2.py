'''A program input name,mark and ph_no of a student and format it using formate function

"The name of the student is bhoomika,marks is 89,ph no is 9999888"    '''

name = (input("enter your name: "))
marks =  int(input("enter your marks: "))
ph_number = int(input("enter your ph no: "))

f= "the name of the student is {}, her marks is {} and phone number is {}".format(name,marks,ph_number)
print(f)