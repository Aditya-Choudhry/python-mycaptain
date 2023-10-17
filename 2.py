import os

# Get the filename from the user
filename = input("Enter the filename: ")

# Get the file extension
extension = os.path.splitext(filename)[1]

# Print the file extension
print("The file extension is:", extension)
