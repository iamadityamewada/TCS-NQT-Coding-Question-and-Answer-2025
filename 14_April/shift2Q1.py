# Q1) Write a program to check whether two given strings are anagrams of each other or not.
# Two strings are said to be anagrams if they contain the same characters in the same frequency, but possibly in a different order.

# Example:
# str1 = ram  
# str2 = mar


str1 = input().lower()
str2 =  input().lower()


def isAnagram(str1, str2):
    if len(str1)!=len(str2):
        return False
    else:
        str1 = sorted(str1)
        str2 = sorted(str2)
        print(str1 , str2)
        if str1 == str2:
            return True
        else:
            return False
        
print(isAnagram(str1,str2))        