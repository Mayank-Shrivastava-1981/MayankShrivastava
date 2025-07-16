user_inputs=input("Enter your inputs:")
numbers = user_inputs.split()
numbers = [int(num) for num in numbers if num.isdigit()]
print("The numbers you entered are:", numbers)


#Counting the occurances of each numberfrom collections import Counter
from collections import Counter
def count_occurrences(numbers):
    return Counter(numbers) 
occurrences = count_occurrences(numbers)
print("Occurrences of each number:", occurrences)


str=input ("Enter a string:")
dict={}
for char in str:
    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
print("Character count in the string:", dict)

# write the program to fine the number is prime or not
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# write the program to chekc the string is palindrome or not
def is_palindrome(s):
    return s == s[::-1]     

# Example usage 
#   num = int(input("Enter a number to check if it's prime: "))
#   print(f"{num} is prime: {is_prime(num)}")   
s = input("Enter a string to check if it's a palindrome: ") 
print(f"{s} is a palindrome: {is_palindrome(s)}")
   


