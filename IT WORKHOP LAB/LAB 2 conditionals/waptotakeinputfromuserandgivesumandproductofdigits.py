n = int(input("Enter the number you wish:"))
sum_ = 0
product_ = 1
while(n!=0):
    ld = n%10
    sum_ = sum_ +ld 
    product_ = product_*ld
    n = n//10
print("The value of the sum of the digits is",sum_)
print("The value of the product of the digits is",product_)