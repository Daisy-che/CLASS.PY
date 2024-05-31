class Animal:
    def make_sound(self):
        pass
    def move(self):
        pass
class Bird(Animal):
    def make_sound(self):
        print("chirp") 
    def move(self) :
        print("The bird is flying")
    def reproduce(self):
        print("Laying eggs")
    def skin(self):
        print("scale")    
class Fish(Animal) :
    def make_sound(self):
        print("click") 
    def move(self):
        print("swimming")
    def reproduce(self):
        print("Laying eggs") 
    def skin(self):
        print("scale")
class Dog(Animal):
    def make_sound(self):
        print("Barking")
    def move(self):
        print("The dog is running")
    def reproduce(self):
        print("The dog give birth")
    def skin(self):
        print("fur")
                            