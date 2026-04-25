# =========================
# STRING PRACTICE QUESTIONS
# =========================
from itertools import count

# 1. Take a string input and:
# - Convert it to uppercase
# - Convert it to lowercase

str = input("Enter a string")
# print(str.upper())
# print(str.lower())

# 2. Take a string and:
# - Print its length
# - Print first and last character
# print(len(str))
# print(str[0], str[-1])

# 3. Take a string and:
# - Reverse it (without using slicing [::-1] if possible)
# reversed_str = "".join(reversed(str))
# print(reversed_str)

# 4. Palindrome Check
# Take a string and check:
# - Is it a palindrome? (madam, racecar)
# if(reversed_str == str):
#     print("the string is palindrome")
# else:
#     print("the string is not palindrome")

# 5. Count Vowels
# Take a string and count number of vowels (a, e, i, o, u)

vowels = "aeiouAEIOU"
count = 0

for char in str:
    if char in vowels:
        count += 1

print(count)

# 6. Replace Words
# Take a sentence and:
# - Replace "Python" with "Django"

new_str = str.replace("python","Django")
print(new_str)

# 7. Remove Spaces
# Take a string and:
# - Remove all spaces


# 8. Count Words
# Take a sentence and:
# - Count total number of words
no_space_str = str.replace(" ","")
print(no_space_str)

# 9. Check Substring
# Take a string and:
# - Check if "code" exists in it

if "code" in str:
    print("yes")
else:
    print(str)

# 10. Format Output (Important for Django)
# Take name and age as input and print:
# "My name is Anubhav and I am 20 years old"
# (Use f-string)


# =========================
# BONUS (IMPORTANT)
# =========================

# 11. Email Slicer
# Take email input:
# example: anubhav@gmail.com
# - Extract username (anubhav)
# - Extract domain (gmail.com)


# 12. Remove Duplicate Characters
# Input: "programming"
# Output: "progamin" (no duplicates)


# =========================
# END
# =========================