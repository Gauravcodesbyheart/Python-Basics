 # By using the init function we can give input to the class
class student:
    def __init__(self,fullname):  # function ke inside me jo parameter aaya hai wo self
        self.name = fullname      #object me jo self aaya hai wo 
s1 = student ("karan")
print(s1.name)        # output will be argument of student ()

s2 = student ("arjun")
print(s2.name)
