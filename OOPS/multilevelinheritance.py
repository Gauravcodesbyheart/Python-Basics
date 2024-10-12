class car:
    @staticmethod
    def start():
        print("car started...")

    @staticmethod
    def close():
        print("car stopped...")


class toyotacar(car):          # here car is inherited by 
    def __init__(self,brand):
        self.brand = brand

class fortuner(toyotacar):    #here toyotacar is inherited by fortuner class
    def __init__(self,type):
        self.type = type

car1 = fortuner("Diesel")
car1.start()
car1.close()