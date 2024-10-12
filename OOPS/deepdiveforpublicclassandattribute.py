class person:
    __name = "anonymous"

    def __hello(self):    # this si made private by the use of __ 
        print("Hello person!")

    def welcome(self):  # here welcome can call hello function but hello can't call welcome
        self.__hello()    # this part is made as public 

p1 = person ()   # here p1 can call welcome 
print(p1.welcome())   #here welcome can be called by p1 object but can't call hello
