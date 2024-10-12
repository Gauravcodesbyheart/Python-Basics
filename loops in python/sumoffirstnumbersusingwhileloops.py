number = int (input("Enter the number upto which you want to sum: "))
sum = 0
i = 1
while i <= number:
    sum += i
    i+=1
print("The sum of number from 1 to ",number,"is ",sum)