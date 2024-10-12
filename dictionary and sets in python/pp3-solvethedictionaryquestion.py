#wap to enter the marks of 3 subjects from the user and store them in a dictionary . start with an empty dictionary and add one by one . use subjects name as key and marks as value
marks = {}
x =  int (input("Enter the  marks of physics: "))
y = int (input("Enter the marks of math: "))
z = int (input("Enter the marks of english: "))
marks.update({"phy" : x}) 
marks.update({"Math" : y})
marks.update({"english" : z})
print(marks)