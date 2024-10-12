n = int(input("Enter the number you wish\n"))
num1 = 0
num2 = 0
count = 0
while(n!=0):
    ld = n % 10
    if (count == 0):
        num1 = ld
    count = count+1
    n = n//10
    if(n==0):
        num2 = ld
sum = num1+num2
print("The sum of first and last digit of the number is ",sum)