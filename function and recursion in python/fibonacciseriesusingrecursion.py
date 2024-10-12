def fibonacci(n):
  """Calculates the nth Fibonacci number recursively."""
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

# Get the desired term from the user
n = int(input("Enter the value of n: "))

# Calculate and print the nth Fibonacci number
result = fibonacci(n)
print("The", n, "th Fibonacci number is:", result)