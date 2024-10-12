mylists = []
size = int(input("Enter the size of the lists"))
for el in range (0,size):
    mylists.append(int(input("Enter the number in the list:")))
print("The elements of the lists are",mylists)
sum1 = 0
for el in range (0,size):
    sum1 = sum1 + mylists[el]

average = sum1 / len(mylists)
print("The average of the",size,"numbers is ",average)