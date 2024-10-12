first_num = int(input("Enter the first number:\n"))
second_num = int(input("Enter the second number:\n"))
third_num = int(input("Enter the third number:\n"))
if (first_num>second_num):
    if(second_num>third_num):
        print(second_num,"is the greatest number")
    else:
        print(third_num,"is the greatest number")
else:
    if(second_num>third_num):
        print(second_num,"is the greatest number")
    else:
        print(third_num,"is the greatest number")