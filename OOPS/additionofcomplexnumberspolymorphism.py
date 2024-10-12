class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img 

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(num1,num2):   # dunder function doinfg this we can get sum by using + symbol
        newreal = num1.real + num2.real
        newimg = num1.img+num2.img
        return complex(newreal,newimg)

num1 = complex(1,3)
num1.shownumber()

num2 =complex(4,6)
num2.shownumber() 

# num3 = num1.add(num2)
num3 = num1 + num2    # dunder function doinfg this we can get sum by using + symbol
num3.shownumber()