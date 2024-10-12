my_list = []
n = 10
for i in range(0,n):
    my_list.append(int(input("Enter the elements of the lists are:\n")))
print("The elements of the list are\n",my_list)
for i in range (0,n):
    if(i%2==0):
        my_list[i] = my_list[i]**2
    else:
        my_list[i] = my_list[i]-1
print("The elments of the list after updation are:\n",my_list)
for i in range(1,len(my_list)):
    key = my_list[i]
    j = i-1
    while j>=0 and key <my_list[j]:
        my_list[j+1] = my_list[j]
        j-=1
    my_list[j+1] = key
print("The elements of the sorted list are:\n",my_list)
print("The smallest element is ",my_list[0],"The greatest elementof the list is ",my_list[9])



