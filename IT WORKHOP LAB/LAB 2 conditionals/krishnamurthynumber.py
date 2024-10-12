num = int(input("Enter the number you wish:"))
temp_num = num
factorial_sum  = 0
while(temp_num!=0):
    ld = temp_num % 10
    factorial = 1
    for el in range (1,ld+1):
        factorial = factorial*el
    temp_num =temp_num//10        
    factorial_sum = factorial_sum + factorial
if (factorial_sum == num):
    print("The given number is a peterson number")
else:
    print("The given number is not a peterson number")

      

