class student :
    def __init__(self,name):
        self.name = name
s1 = student("Gaurav Singh")
print(s1.name)   #here value of s1.name is printed 
del s1.name      #here value of s1 is deleted
print(s1.name)        #value of s1 already deleted so nothing printed more 