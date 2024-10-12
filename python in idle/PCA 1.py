my_lists = []
n = 10
max_count = 0
max_element = None
my_lists.append(0)
my_lists.append(1)
for i in range (2,n+1):
    my_lists.append(my_lists[i-1]+my_lists[i-2])
print("The elements of the lists are\n",my_lists)
for element in range (0,10):
    count = 0
    for item in my_lists:
        if element == item:
            count = count+1
        if count > max_count:
            max_count = count
            max_element = element
print("The element having the maximum frequency is",max_element)
            
    
