# TCS NQT-2025 – 31st March 2025 (1st Shift Coding Question)
# Q1)
# Write a program that reads a string input from the user and removes all consecutive duplicate characters while maintaining the original order of distinct characters.
# The program should then output the modified string.

# Example:
# Input:
# 223334566777
# Output:
# 234567


str1 = input()

new_str = []

for i in str1:
    if i in new_str:
        pass
    else:
        new_str.append(i)

new_str = "".join(new_str)      

print(new_str)


# s = input("Enter the string: ")
# result = []

# for ch in s:
#     if not result or ch != result[-1]:  # check if result is empty or ch != last added char
#         result.append(ch)

# print(''.join(result))


# # Read input string
# s = input("Enter the string: ")

# # Initialize the result with the first character
# result = s[0] if s else ""

# # Loop through the rest of the string
# for i in range(1, len(s)):
#     if s[i] != s[i - 1]:
#         result += s[i]

# # Print the result
# print(result)


