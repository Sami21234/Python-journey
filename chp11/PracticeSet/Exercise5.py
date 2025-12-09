
# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no. of seats) and get fare information of train running under Indian Railways. 

# import random or
from random import randint

class Train:

    def __init__(self, trainNO):
       self.trainNO = trainNO 

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