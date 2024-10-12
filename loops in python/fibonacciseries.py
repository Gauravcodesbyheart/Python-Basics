term_1 = 0
term_2 = 1
sum = 1
number_of_term = int(input("Enter the number of term that you want to print in fibonacci series:"))
for el in range (1,number_of_term):
    term_1 = term_2
    term_2 = sum
    sum = term_1 + term_2
print("The value of ",number_of_term,"th term of the fibonacci series is ",term_1)