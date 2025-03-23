# Problem Statement:
# Given a range [m, n] (both inclusive) where 0 <= m, n <= 10000, find the sum of all integers between m and n.

# Example:
# Input:
# 0 3
# Output:
# 6
# Explanation:
# 0+1+2+3 = 6


x,y = map(int, input().split())

sum = 0
for i in range(x, y+1):
    sum += i
print(sum)  
