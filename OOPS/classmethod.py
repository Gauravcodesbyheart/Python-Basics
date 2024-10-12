# class person:
#     name = "anonymous"

#     def changename(self,name):
#      person.name = name   # this creates new name for the attribute for my instance for my object

# p1 = person ()
# p1.changename("Rahul kumar")
# print(p1.name)
# print(person.name)


class car:
   name = "NULL"

   @classmethod    
   def changename(cls,name):
    cls.name = name
     # notice the difference via to first code we can clearly notice here 
      
c1 = car()
c1.changename("Mercedes Maybeach")
print(c1.name)
print(car.name)
   