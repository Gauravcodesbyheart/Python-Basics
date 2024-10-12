my_list = []
n = 10
for i in range (0,n):
    my_list.append(int(input("Enter a term:")))
print(my_list)
for i in range (0,len(my_list)):
    if i % 2 == 0:
        my_list[i] = my_list[i]*2
    else:
        my_list[i] = my_list[i]-1
print("The elements of the list after updation are:",my_list)
print("The minimum element in the updated list is:",my_list[0])
print("The maximum element in the updated list is:",my_list[9])
high = len(my_list)-1
low = 0
key = int(input("Enter the number to be searched in the updated list :"))
while low<=high:
    mid = (low+high)//2
    if key == my_list[mid]:
        new_mylist = []
        new_mylist.append(mid)
        lb,ub = mid,mid
        count = 1
        while (lb!=0 or ub!=0 and lb>low and ub<high):
            if 

