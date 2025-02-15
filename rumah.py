class house:
    def __init__(self,square,color,room,floor,location):
        self.square = square
        self.color = color
        self.room = room
        self.floor = floor
        self.location = location

    def tampilkan_rumah (self):
        print ("location")
    
myhouse = house ("1000","white","3 room","3 floor","cicurug")
print (myhouse.location)
myhouse.tampilkan_rumah ()