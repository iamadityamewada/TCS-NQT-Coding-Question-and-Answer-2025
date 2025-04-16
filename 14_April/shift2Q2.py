# Q2) Question: Standard Deviation of an Array
# Problem Statement:
# Write a  program to calculate the standard deviation of a given array of integers.

# 📐 Formula:
# The formula for standard deviation is:

# (Standard deviation formula is assumed but not shown in the image — likely:
# SD = sqrt(Σ(xᵢ - mean)² / n))

# ✅ Your program should:
# Read an integer n representing the number of elements in the array.

# Read n integers.

# Calculate the mean of the array.

# Use the mean to compute the standard deviation.

# Print the standard deviation rounded to 2 decimal places.

# 🧾 Input Format:
# First line: An integer n (number of elements)

# Second line: n space-separated integers

n = int(input())
arr = list(map(int, input().split()))
# arr = input().split()
print(arr)

mean = 0

for i in arr:
    mean += int(i)
mean = mean/n

sum = 0
for i in arr:
    sum = sum + (int(i)-mean)**2

sd = ((sum/n)**0.5)

print(f"{sd:.2f}")



