# Q2) Subset Sum Problem
# You are given an array of integers and a target sum h. Your task is to determine whether any subset of the given numbers can sum up to h.

# If a valid subset exists, print "Yes"

# Otherwise, print "No"

# Constraints:
# 1 ≤ t ≤ 100 (Number of elements in the array)

# 1 ≤ timeslot[i] ≤ 1000 (Values in the array)

# 1 ≤ h ≤ 10000 (Target sum)

# Example Run:
# Enter number of elements in timeslot[]: 4  
# Enter 4 elements:  
# 3 5 7 2  
# Enter the target sum (h): 10  
# Expected Output:
# Yes




def is_subset_sum(arr, n, target, memo):
    # Base cases
    if target == 0:
        return True
    if n == 0:
        return False

    # Check if already computed
    if (n, target) in memo:
        return memo[(n, target)]

    # If current element is greater than target, skip it
    if arr[n - 1] > target:
        memo[(n, target)] = is_subset_sum(arr, n - 1, target, memo)
    else:
        # Include or exclude the current element
        memo[(n, target)] = (is_subset_sum(arr, n - 1, target, memo) or
                             is_subset_sum(arr, n - 1, target - arr[n - 1], memo))

    return memo[(n, target)]

# Input handling
t = int(input("Enter number of elements in timeslot[]: "))
print(f"Enter {t} elements:")
arr = list(map(int, input().split()))
h = int(input("Enter the target sum (h): "))

# Function call with memoization
memo = {}
if is_subset_sum(arr, len(arr), h, memo):
    print("Yes")
else:
    print("No")
