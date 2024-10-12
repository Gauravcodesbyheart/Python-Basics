num = int(input("Enter the number you wish: "))
num1 = num
sum_ = 0
while(num!=0):
    ld = num%10
    sum_ = sum_ + ld**3
    num = num//10
if (num1 == sum_):
    print("The given number is a armstrong number.")
else:
    print("The given number is not a armstong number")
