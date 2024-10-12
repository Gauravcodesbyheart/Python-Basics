#figure out a way to store 9 and 9.0 as separate values in the set. (you can take the help of built in data type])
values = {2,2.0}
print(values) # returns only 2 as considers 2 and 2.0 as same values
# we can use strings to store these two as different
values1 = {9,"9.0"}
print(values1) # another possible solution for this is ---
values2 = {
    ("float",9.0),
    ("int",9),
}
print(values2)