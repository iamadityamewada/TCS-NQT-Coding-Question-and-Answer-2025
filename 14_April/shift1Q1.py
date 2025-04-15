# Q1) You are given two integers m and n. Your task is to compute the sum of the m-th prime number to the (m + n)-th prime number, inclusive.
# Input:
# Two integers m and n such that m ≥ 1 and n ≥ 0.

# Output:
# Print the sum of the m-th, (m+1)-th, ..., (m+n)-th prime numbers.

# Example 1:
# Input:

# m = 2  
# n = 2
# Output:

# Sum = 15
# Explanation:

# 2nd prime = 3

# 3rd prime = 5

# 4th prime = 7

# Sum = 3 + 5 + 7 = 15

m,n = input().split()
m = int(m)
n = int(n)

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def findNthPrime(n):
    count = 0
    num = 2
    while count < n:
        if isPrime(num):
            count+=1
        if count == n:
            return num
        num+=1

sum = 0

for i in range(m, (m+n)+1):
    print(findNthPrime(i))
    sum = sum + findNthPrime(i)

print(sum)