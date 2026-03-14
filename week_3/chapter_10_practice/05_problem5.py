from random import randint

class Train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,Fro,To):
        print(f"your ticket is booked for trainNo: {self.trainNo} from {Fro} to {To} ")
    def getstatus(self):
        print(f"trainNo: {self.trainNo} is booked and currently in RAC")
    def getfare(self,Fro,To):
        print(f"your trainNo: {self.trainNo} fare from {Fro} to {To} is {randint(250,550)}")

t=Train(56895)
t.book("kt" , "bng")
t.getstatus()
t.getfare("kt" , "bng")

    