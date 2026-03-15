class emp:
    a=1

    @classmethod    #it shows the class attribute instead of instance attribute
    def show(cls):
        print(f"the class attri of a is: {cls.a}")

e=emp()
e.a=65  #instance attri
e.show()
