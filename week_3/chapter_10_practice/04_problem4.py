class calculator:
    def __init__(self,n):
        self.n=n
    
    @staticmethod
    def greet():
        print("hello")
        
    def square(self):
        print(f"the square is {self.n*self.n}")
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")

p=calculator(6)
p.greet()
p.square()
p.cube()
p.squareroot() 
