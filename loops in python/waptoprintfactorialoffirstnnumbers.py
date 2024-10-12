number = int (input("Enter the number upto which you want to sum: "))
product  = 1
i = 1
while i <= number:
    product *= i
    i+=1
print("The product of number from 1 to ",number,"is ",product)