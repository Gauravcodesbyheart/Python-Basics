class student:
    college_name = "ABC College"    #it stores here only once in the class 
    def __init__(self):             #default constructor
        pass
    def __init__(self,name,marks): # parametrized constructor
        self.name = name
        self.marks = marks
        print("Adding new student in Database")
s1 = student("karan",97)

print(s1.name, s1.marks)      

s2 = student("Arjun",99)
print(s2.name, s2.marks)
print(s2.college_name)  #using this both we came to a common result
print(student.college_name)  # here class.variable