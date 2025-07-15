# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Outer while loop for each row
while row < size:
    # Inner for loop for each column in the row
    for col in range(size):
        print("*", end=" ")
    print()  # Newline after each row
    row += 1