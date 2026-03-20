#create a class "pets" from a class "animals" and further create a class "dog" from "pets" add a method "bark" to class "dog"

class animals:
    def __int__(self,i,j):
        self.i=i
        self.j=j

class pets(animals):
    def __int__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

class dog(pets):

    @staticmethod
    def bark():
        print("the dog barks bow")

d=dog()
d.bark()

    