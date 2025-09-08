import random
class Train:
    def __init__(self,trainno,fro,to):
        self.trainno=trainno
        self.fro=fro
        self.to=to
    def bookTicket(self):
        print(f"Ticket is booked for {self.trainno} from {self.fro} to {self.to}")
    def getStatus(self):
        print(f"Train no {self.trainno} is running on time")
    def fareInfo(self):
        print(f"Ticket fare in train no {self.trainno} from {self.fro} to {self.to} is Rs.{random.randint(22,5555)}") 
t=Train(1234,"bbsr","raipur")
t.bookTicket()       
t.getStatus()
t.fareInfo()