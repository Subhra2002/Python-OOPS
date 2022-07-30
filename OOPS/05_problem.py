class Train:
    def __init__(self,name,price,seats):
        self.name = name
        self.price = price
        self.seats = seats
    
    def getStatus(self):
        print(f"The name of a train is {self.name}")
        print(f"The number of available seats  is {self.seats}")
    
    def fareInfo(self):
        print(f"The price is RS -{self.price}")

    def bookTicket(self):
        if (self.seats > 0):
            print(f"Your ticket is booked and your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("GOOD BYE KHATAM")
     

intercity = Train("Rajdhani Express : 145098",90,500)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()