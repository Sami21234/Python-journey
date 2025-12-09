
# 6. Can you change the self-parameter inside a class to something else (say “harry”). Try changing self to “slf” or “harry” and see the effects. 

# The answer is no the program will not be changed cause we can take any name instead of self

# import random or
from random import randint

class Train:

    def __init__(slf, trainNO):
       slf.trainNO = trainNO 

    def book(self, fro, to):
        print(f"Ticket is Booked in train no: {self.trainNO} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNO} is running on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNO} from {fro} to {to} is {randint(222,5555)}")

t = Train(12345)
t.book("Bandra", "Boisar")
t.getStatus()
t.getFare("Bandra", "Boisar")
