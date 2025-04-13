# TCS NQT 9th April 2025 Coding Questions

# Q1) Write a program that takes a single input string of space-separated integers, where:
# - The first two numbers indicate the number of rows (m) and columns (n) of a matrix.
# - The rest of the numbers represent the matrix elements (ages as non-negative integers).

# Conditions to handle:
# - If the number of elements provided is more than m x n, print "Wrong input".
# - Otherwise, construct the matrix and check if each row has at least one prime number.
#   - If all rows contain at least one prime, print: "Valid"
#   - If any row does not contain a prime, print: "Not Valid"

# Example:

# Input:
# 2 2 3 4 5 6

# Explanation:
# - row = 2, col = 2
#   So we need a 2 x 2 matrix:

# 3 4
# 5 6

# Breakdown:
# numbers = [2, 2, 3, 4, 5, 6]
# m = 2, n = 2 → matrix = 2x2

# matrix[0][0] = 3
# matrix[0][1] = 4
# matrix[1][0] = 5
# matrix[1][1] = 6

# So, the matrix becomes:

# 3 4
# 5 6

# - Row 1 → has prime (3)
# - Row 2 → has prime (5)

# Output:
# Valid


def isPrime(n):
    """Returns True if n is a prime number, False otherwise."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

inp = input()

# Split input into a list of integers
numbers = list(map(int, inp.split()))

# Extract the number of rows (m) and columns (n)
m = numbers[0]
n = numbers[1]

# The rest are matrix elements
matrix_elements = numbers[2:]

# Check if the number of elements matches m * n
if len(matrix_elements) != m * n:
    print("Wrong input")
else:
    # Create the matrix
    matrix = []
    index = 0
    for i in range(m):
        row = []
        for j in range(n):
            row.append(matrix_elements[index])
            index += 1
        matrix.append(row)

    # Check each row for prime numbers
    for row in matrix:
        if not any(isPrime(num) for num in row):
            print("Not Valid")
            break
    else:
        # If all rows are valid, print "Valid"
        print("Valid")

                



