class Vehicle:
    def __init__(self,make,model,color):
        self.make= make
        self.model=model
        self.color=color
    def move(self):
        print("start moving")
    def hoot(self):
        print("Hink Honk")

class Bus(Vehicle):

    def __init__(make,model,color ,capacity):
         super().__init__(make,model,color)
         self.capacity= capacity
    def start_boarding(self):
        print("the bus is boarding now")
class Lory(Vehicle):
    def __init__(make,model,color,max_load):
        super().__init__(make,model,color)
        self.max_load=max_load
    def load(self):
        print("start loading")    
