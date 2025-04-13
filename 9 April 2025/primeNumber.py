# Q2)

# Write a program to perform the following:

# Take two positive integers m and n as input.

# Find the m-th prime number and the n-th prime number.

# For each of these two prime numbers, calculate the sum of its single-digit numbers (i.e., less than 10). Let these results be m1 and n1.

# Finally, print the value of m * m1.

# Example:
# For input m = 5 and n = 6:

# Prime number sequence: 2, 3, 5, 7, 11, 13

# 5th prime = 11 → digit sum = 1 + 1 = 2 → m1 = 2

# 6th prime = 13 → digit sum = 1 + 3 = 4 → n1 = 4

# Final answer → m * m1 = 5 * 2 = 10


inp = input().split()
nth = int(inp[0])
mth = int(inp[1])

def isPrime(n):
    if n <=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
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

def sumDigit(num):
    if len(str(num))==1:
        return num
    total = 0
    while len(str(num))>1:
        while num>0:
            total += num%10
            num = num//10
    return total        

n = findNthPrime(nth)
m = findNthPrime(mth)

m = sumDigit(m)
n = sumDigit(n)

print(m*n)
        
                       
        