def factorial(number):
    i = 1
    fact = 1
    while i <= number :
        fact = fact*i
        i+=1
    print(fact)   
factorial(int(input("Enter the number: ")))

