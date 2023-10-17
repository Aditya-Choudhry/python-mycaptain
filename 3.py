def fibonacci(n):
  """Calculates the nth Fibonacci number.
  Args:
    n: The term number.
  Returns:
    The nth Fibonacci number.
  """
  a = 0
  b = 1
  for i in range(n):
    next_term = a + b
    a = b
    b = next_term
  return a
# Get the number of terms from the user
n = int(input("Enter the number of terms: "))

# Print the Fibonacci sequence
for i in range(n):
  print(fibonacci(i))
