class student : 
      # creation of class  here no init function is there so python itself creates init function
    def __init__(self):   # constructor always demands for self parameter
        print("Adding new student in database")
    name = "Gaurav singh"

s1 = student()    # creation of object
print(s1.name)
print (s1)

print("creation_of_car_class") 
class car :
    name = "Mercedes maybeach"
    color = "blue"
car1 = car()
print(car1.name)
print(car1.color)
print(car1)