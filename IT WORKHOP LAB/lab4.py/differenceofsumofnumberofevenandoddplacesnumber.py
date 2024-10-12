n = int(input("Enter the number you wish:\n"))
even_sum = 0
odd_sum = 0
count = 0
while(n!=0):
    ld = n % 10
    n = n // 10
    count = count + 1
    if (count % 2 == 0):
        even_sum = even_sum+ld
    else:
        odd_sum = odd_sum+ld
difference = even_sum - odd_sum
print("The difference of sum of digits at even places and odd place is ",difference)
if (difference<0):
    print("The sum of odd place digits is superior")
elif(difference>0):
    print("The sum of even place digits is superior")
else:
    print("The difference of digits at both even places and odd places is 0")