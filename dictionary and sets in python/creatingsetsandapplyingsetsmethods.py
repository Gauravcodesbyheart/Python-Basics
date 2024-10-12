collection = {1,2,3,4, "hello", "world",2,3} # we can also put strings in the sets , sets ignores all the elements which repeats basically considers only unique element
print(collection)
print(type(collection))
(collection.add(10))
print(collection)
(collection.remove(4))
print(collection)
(collection.clear())
print(collection)
set1 = {1,2,3}
set2 = {4,2,6} 
print(set1.union(set2))
print(set1.intersection(set2))