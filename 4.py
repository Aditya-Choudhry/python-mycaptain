def print_positive_numbers(array):
  """Prints all the positive numbers in a given array.

  Args:
    array: A list of numbers.
  """

  for number in array:
    if number > 0:
      print(number)


# Get the array from the user
array = input("Enter the array: ").split()

# Print all the positive numbers in the array
print_positive_numbers(array)
