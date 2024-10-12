class car :
    @staticmethod   #Static methods in Python are used when you want to define a method that belongs to the class rather than an instance of the class. These methods do not require access to the instance or class's state or attributes, making them useful for utility functions that perform operations related to the class, but do not need to manipulate class or instance data. Essentially, static methods can be called on the class itself without needing an object instantiation.
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")
class Toyotacar(car):    # toyotacar me car ki properties inherited
    def __init__(self,name): 
        self.name = name 
 
car1 = Toyotacar("fortuner")
car2 = Toyotacar("prius")

print(car1.start())