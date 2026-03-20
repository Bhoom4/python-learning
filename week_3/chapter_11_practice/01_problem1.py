class twoDvector:
    def __init__(self,i,j):
        self.i=i
        self.j=j

    def show(self):
        print(f"the vector is {self.i}i + {self.j}j ")


class threeDvector(twoDvector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k=k

    def show(self):
        print(f"the vectore is {self.i}i + {self.j}j + {self.k}k")
    

o=twoDvector(1,2)
o.show()
h=threeDvector(1,2,3)
h.show()