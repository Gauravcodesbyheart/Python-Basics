class car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("car stopped...")

class toyotacar(car):   # here using this car is inherited
    def __init__(self,name,type):
        super().__init__(type)   # using this type parameter that is passed as argument is being called and used using the super function
        self.name = name
        super().start()

car1 = toyotacar("prius","electric")
print(car1.type)
 
