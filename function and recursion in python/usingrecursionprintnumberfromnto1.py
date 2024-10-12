def recursion (num):
    if (num==0):
        return 
    print(num)
    recursion(num-1)

recursion(int(input("Enter the number:")))
print("End")