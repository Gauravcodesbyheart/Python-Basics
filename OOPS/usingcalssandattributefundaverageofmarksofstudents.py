class student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_avg(self): 
        sum = 0
        for val in self.marks:
            sum +=val
    print("Hi! Your average score is:",sum /3)     
            
s1 = student("Tony stark",[99,98,97])    

     
          