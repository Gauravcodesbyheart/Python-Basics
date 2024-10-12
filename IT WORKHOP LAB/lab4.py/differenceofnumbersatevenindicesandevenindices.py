mylists = []
size = int(input("Enter the size of the list:\n"))
for i in range(0,size):
    mylists.append(int(input("Enter the items in the list")))
print("The elements of the lists are",mylists)
even_sum = 0
odd_sum = 0
for i in range (0,size):
    if (i%2==0):
        even_sum = even_sum +mylists[i]
    else:
        odd_sum = odd_sum + mylists[i]
difference = even_sum - odd_sum
print("The difference between numbers at even and odd position is ",difference)
        
