a=10
b=20
c=20.4
d="Mayank"
e=True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
type(c)
type(d) 
type(e)


## Strings

str1 = "Hello"
str2 = 'World'      
str3 = """This is a multiline string."""
str4 = '''This is also a multiline string.'''

print(str1)
print(str2) 
print(str3)
print(str4) 
# String concatenation
str5 = str1 + " " + str2    
print(str5)  # Output: Hello World

# String formatting
name = "Alice"      
age = 30
formatted_str = f"My name is {name} and I am {age} years old."
print(formatted_str)  # Output: My name is Alice and I am 30 years old.
# String methods
print(str1.upper())  # Output: HELLO    
print(str2.lower())  # Output: world
print(str3.replace("multiline", "single line"))  # Output: This is a
# single line string.   
print(str4.split())  # Output: ['This', 'is', 'also', 'a', 'multiline', 'string.']  
# String indexing and slicing
print(str1[0])  # Output: H 
print(str2[-1])  # Output: d
print(str3[0:4])  # Output: This    

# String length
print(len(str4))  # Output: 38
# String membership
print("Hello" in str1)  # Output: True
print("World" not in str2)  # Output: False 
# String iteration
for char in str1:
    print(char, end=" ")  # Output: H e l l o   
# String comparison
print(str1 == "Hello")  # Output: True  
print(str2 != "World")  # Output: False
# String escape characters
str6 = "This is a string with a newline character.\nAnd this is on a new line."
print(str6)  # Output: This is a string with a newline character.   # And this is on a new line.    

# String immutability
str7 = "Immutable"  

try:
    str7[0] = "i"  # This will raise an error because strings are immutable 

except TypeError as e:
    print(f"Error: {e}")        

# String concatenation with numbers
num1 = 5
num2 = 10   

str8 = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(num1 + num2)
print(str8)  # Output: The sum of 5 and 10 is 15
# String formatting with numbers
formatted_num_str = f"The sum of {num1} and {num2} is {num1 + num2}"
print(formatted_num_str)  # Output: The sum of 5 and 10 is 15   
# String methods with numbers
num_str = "12345"   
print(num_str.isdigit())  # Output: True
print(num_str.isalpha())  # Output: False       
print(num_str.isalnum())  # Output: True
# String methods with special characters
special_str = "Hello@123"   
print(special_str.isalnum())  # Output: False
print(special_str.isalpha())  # Output: False   
print(special_str.isdigit())  # Output: False
# String methods with whitespace
whitespace_str = "   Hello World   "    
print(whitespace_str.strip())  # Output: Hello World
print(whitespace_str.lstrip())  # Output: Hello World   

print(whitespace_str.rstrip())  # Output:    Hello World
# String methods with case sensitivity  
case_str = "Hello World"
print(case_str.lower())  # Output: hello world      

print(case_str.upper())  # Output: HELLO WORLD
print(case_str.title())  # Output: Hello World  
print(case_str.capitalize())  # Output: Hello world
# String methods with searching
search_str = "Hello World"  
print(search_str.find("World"))  # Output: 6        
print(search_str.index("Hello"))  # Output: 0
print(search_str.count("o"))  # Output: 2   
# String methods with splitting and joining
split_str = "apple,banana,cherry"   
print(split_str.split(","))  # Output: ['apple', 'banana', 'cherry']
join_str = ["apple", "banana", "cherry"]    

print(", ".join(join_str))  # Output: apple, banana, cherry
# String methods with formatting

formatted_str2 = "The value of pi is approximately {:.2f}".format(3.14159)  
print(formatted_str2)  # Output: The value of pi is approximately 3.14
# String methods with encoding and decoding
encoded_str = "Hello World".encode("utf-8") 

print(encoded_str)  # Output: b'Hello World'
decoded_str = encoded_str.decode("utf-8")
print(decoded_str)  # Output: Hello World
# String methods with checking
print("Hello".isalpha())  # Output: True
print("123".isdigit())  # Output: True
print("Hello123".isalnum())  # Output: True
print("Hello World".isspace())  # Output: False
print("   ".isspace())  # Output: True
# String methods with replacing
replaced_str = "Hello World".replace("World", "Python")
print(replaced_str)  # Output: Hello Python
# String methods with counting
count_str = "Hello World"

print(count_str.count("o"))  # Output: 2
print(count_str.count("l"))  # Output: 3        
# String methods with checking starts and ends
print("Hello World".startswith("Hello"))  # Output: True
print("Hello World".endswith("World"))  # Output: True
# String methods with checking starts and ends with different cases
print("Hello World".startswith("hello"))  # Output: False
print("Hello World".endswith("world"))  # Output: False
# String methods with checking starts and ends with different cases
print("Hello World".lower().startswith("hello"))  # Output: True
print("Hello World".upper().endswith("WORLD"))  # Output: True
# String methods with checking starts and ends with different cases
print("Hello World".capitalize().startswith("Hello"))  # Output: True
print("Hello World".title().endswith("World"))  # Output: True  
# String methods with checking starts and ends with different cases
print("Hello World".swapcase().startswith("hELLO wORLD"))  # Output: True
print("Hello World".swapcase().endswith("wORLD hELLO"))  # Output: True 
# String methods with checking starts and ends with different cases
print("Hello World".casefold().startswith("hello"))  # Output: True

print("Hello World".casefold().endswith("world"))  # Output: True
# String methods with checking starts and ends with different cases 

print("Hello World".removeprefix("Hello "))  # Output: World
print("Hello World".removesuffix(" World"))  # Output: Hello    
# String methods with checking starts and ends with different cases
print("Hello World".removeprefix("hello "))  # Output: Hello World      
print("Hello World".removesuffix("world"))  # Output: Hello World
# String methods with checking starts and ends with different cases 
print("Hello World".removeprefix("Hello"))  # Output:  World
print("Hello World".removesuffix("World"))  # Output: Hello 
# String methods with checking starts and ends with different cases
print("Hello World".removeprefix("hello"))  # Output: Hello World   

print("Hello World".removesuffix("world"))  # Output: Hello World
# String methods with checking starts and ends with different cases 

print("Hello World".removeprefix("Hello "))  # Output: World
print("Hello World".removesuffix(" World"))  # Output: Hello    


# String methods with checking starts and ends with different cases

print("Hello World".removeprefix("hello "))  # Output: Hello World
print("Hello World".removesuffix("world"))  # Output: Hello World

#Sequences
# List  

my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# List with mixed data types    
#   my_mixed_list = [1, "Hello", 3.14, True]        
my_mixed_list = [1, "Hello", 3.14, True]
print(my_mixed_list)  # Output: [1, 'Hello', 3.14, True]    

# List with nested lists
nested_list = [1, 2, [3, 4], 5] 

print(nested_list)  # Output: [1, 2, [3, 4], 5]
# Accessing elements in a list
print(my_list[0])  # Output: 1  
print(my_list[1])  # Output: 2
print(my_list[-1])  # Output: 5  (last element) 
print(nested_list[2][0])  # Output: 3 (accessing nested list element)
print(nested_list[2][1])  # Output: 4 (accessing nested list element)

# Slicing a list    

print(my_list[1:4])  # Output: [2, 3, 4] (elements from index 1 to 3)
print(my_list[:3])  # Output: [1, 2, 3] # (elements from start to index 2)
print(my_list[2:])  # Output: [3, 4, 5]  # (elements from index 2 to end)
print(my_list[-3:])  # Output: [3, 4, 5]  # (last three elements)
print(my_list[:-2])  # Output: [1, 2, 3]  # (all elements except the last two)
print(nested_list[1:3])  # Output: [2, [3, 4]]  # (elements from index 1 to 2 in nested list)
print(nested_list[:2])  # Output: [1, 2]  # (elements from start to index 1 in nested list)
print(nested_list[2:])  # Output: [[3, 4], 5]  # (elements from index 2 to end in nested list)
print(nested_list[-2:])  # Output: [[3, 4], 5]  # (last two elements in nested list)
print(nested_list[:-1])  # Output: [1, 2, [3, 4]]  # (all elements except the last one in nested list)      
# Modifying a list  
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]  
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]
my_list.insert(1, 15)               

print(my_list)  # Output: [10, 15, 2, 3, 4, 5, 6]
my_list.remove(3)   
print(my_list)  # Output: [10, 15, 2, 4, 5, 6]
my_list.pop()   
print(my_list)  # Output: [10, 15, 2, 4, 5]  # removes the last element
my_list.pop(1)  # removes the element at index 1    
print(my_list)  # Output: [10, 2, 4, 5]  # removes the element at index 1
my_list.extend([7, 8, 9])
print(my_list)  # Output: [10, 2, 4, 5, 7, 8, 9]  # extends the list with new elements
my_list.sort()
print(my_list)  # Output: [2, 4, 5, 7, 8, 9, 10]  # sorts the list in ascending order
my_list.reverse()
print(my_list)  # Output: [10, 9, 8, 7, 5, 4, 2]  # reverses the order of elements in the list
# List methods  
print(len(my_list))  # Output: 7  # returns the length of the list
print(my_list.count(2))  # Output: 1  # counts the occurrences of the element 2 in the list
print(my_list.index(4))  # Output: 4  # returns the index of    the first occurrence of the element 4 in the list   
print(my_list.index(10))  # Output: 0  # returns the index of the first occurrence of the element 10 in the list
print(my_list.index(5))  # Output: 5  # returns the index of the first occurrence of the element 5 in the list
print(my_list.index(7))  # Output: 3  # returns the index of    the first occurrence of the element 7 in the list
print(my_list.index(8))  # Output: 2  # returns the index of the first occurrence of the element 8 in the list
print(my_list.index(9))  # Output: 1  # returns the index of    the first occurrence of the element 9 in the list
print(my_list.index(10))  # Output: 0  # returns the index of the first occurrence of the element 10 in the list
print(my_list.index(2))  # Output: 6  # returns the index of the first occurrence of the element 2 in the list
print(my_list.index(4))  # Output: 3  # returns the index of    the first occurrence of the element 4 in the list
print(my_list.index(5))  # Output: 4  # returns the index of the first occurrence of the element 5 in the list
print(my_list.index(7))  # Output: 5  # returns the index of the first occurrence of the element 7 in the list
print(my_list.index(8))  # Output: 2  # returns the index of the first occurrence of the element 8 in the list
print(my_list.index(9))  # Output: 1  # returns the index of    the first occurrence of the element 9 in the list
print(my_list.index(10))  # Output: 0  # returns the index of   the first occurrence of the element 10 in the list
# List comprehension
squared_list = [x**2 for x in my_list if isinstance(x, int)]
print(squared_list)  # Output: [100, 4, 16, 25, 49, 64, 81]  # squares of elements in the list
# List comprehension with conditions    
even_list = [x for x in my_list if x % 2 == 0]  
print(even_list)  # Output: [2, 4, 8, 10]  # even elements in the list
odd_list = [x for x in my_list if x % 2 != 0]   
print(odd_list)  # Output: [9, 7, 5]  # odd elements in the list
# List comprehension with nested lists  
nested_list_comp = [[x**2 for x in sublist] for sublist in nested_list if isinstance(sublist, list)]
print(nested_list_comp)  # Output: [[9, 16]]  # squares of elements in nested lists
# List comprehension with nested lists and conditions   
nested_even_list_comp = [[x for x in sublist if x % 2 == 0] for sublist in nested_list if isinstance(sublist, list)]
print(nested_even_list_comp)  # Output: [[4]]  # even elements in nested lists
nested_odd_list_comp = [[x for x in sublist if x % 2 != 0] for sublist in nested_list if isinstance(sublist, list)]
print(nested_odd_list_comp)  # Output: [[3]]  # odd elements in nested lists    
# List comprehension with nested lists and conditions
nested_mixed_list_comp = [[x for x in sublist if isinstance(x, int)] for sublist in nested_list if isinstance(sublist, list)]
print(nested_mixed_list_comp)  # Output: [[3, 4]]  # mixed elements in nested lists


# function in python
def greet(name):    
    """Function to greet a person."""
    return f"Hello, {name}!"    
# Calling the function
print(greet("Alice"))  # Output: Hello, Alice!      
# Function with default parameter
def greet_with_default(name="World"):
    """Function to greet a person with a default name."""
    return f"Hello, {name}!"    
# Calling the function with default parameter
print(greet_with_default())  # Output: Hello, World!    
# Function with multiple parameters
def add_numbers(a, b):
    """Function to add two numbers."""
    return a + b
# Calling the function with multiple parameters
print(add_numbers(5, 10))  # Output: 15 
# Function with variable number of arguments
def add_multiple_numbers(*args):
    """Function to add multiple numbers."""
    return sum(args)
# Calling the function with variable number of arguments
print(add_multiple_numbers(1, 2, 3, 4, 5))  # Output: 15


# Function with keyword arguments
def print_info(name, age):  
    """Function to print name and age."""
    print(f"Name: {name}, Age: {age}")      
# Calling the function with keyword arguments
print_info(name="Alice", age=30)  # Output: Name: Alice, Age: 30
# Function with default and keyword arguments
def print_info_with_default(name="Unknown", age=0):
    """Function to print name and age with default values."""
    print(f"Name: {name}, Age: {age}")  
# Calling the function with default and keyword arguments
print_info_with_default()  # Output: Name: Unknown, Age: 0
# Function with return value
def multiply(a, b):
    """Function to multiply two numbers."""
    return a * b    
# Calling the function with return value
result = multiply(5, 10)

print(result)  # Output: 50
# Function with return value and multiple return statements
def divide(a, b):
    """Function to divide two numbers."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b        

# Calling the function with return value and multiple return statements
print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Cannot divide by zero
# Function with lambda expression
multiply_lambda = lambda x, y: x * y
# Calling the lambda function
print(multiply_lambda(5, 10))  # Output: 50

# Function with nested functions
def outer_function(x):
    """Outer function with a nested function."""
    def inner_function(y):
        """Inner function to multiply x and y."""
        return x * y
    return inner_function       
# Calling the outer function with a nested function
inner_func = outer_function(5)

print(inner_func(10))  # Output: 50  # calling the inner function with y=10
# Function with decorators  
def decorator_function(func):
    """Decorator function to modify the behavior of another function."""
    def wrapper(*args, **kwargs):
        print("Before calling the function")
        result = func(*args, **kwargs)
        print("After calling the function")
        return result
    return wrapper      

@decorator_function
def say_hello(name):
    """Function to say hello."""
    return f"Hello, {name}!"    
# Calling the decorated function
print(say_hello("Alice"))  # Output: Before calling the function

# Hello, Alice! After calling the function

# Function with recursion
def factorial(n):
    """Function to calculate the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)     

# Calling the recursive function
print(factorial(5))  # Output: 120  # factorial of 5 is 120
# Function with error handling
def divide_with_error_handling(a, b):
    """Function to divide two numbers with error handling."""
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input type" 
# Calling the function with error handling
print(divide_with_error_handling(10, 2))  # Output: 5.0
print(divide_with_error_handling(10, 0))  # Output: Cannot divide by zero
print(divide_with_error_handling(10, "a"))  # Output: Invalid input type    


# Function with type hints  
def add_numbers_with_type_hints(a: int, b: int) -> int:
    """Function to add two numbers with type hints."""
    return a + b    
# Calling the function with type hints
print(add_numbers_with_type_hints(5, 10))  # Output: 15

# Function with type hints and default parameters  
def greet_with_type_hints(name: str = "World") -> str:
    """Function to greet a person with type hints."""
    return f"Hello, {name}!"
# Calling the function with type hints and default parameters   
print(greet_with_type_hints())  # Output: Hello, World!
# Function with type hints and variable number of arguments

def add_multiple_numbers_with_type_hints(*args: int) -> int:
    """Function to add multiple numbers with type hints."""
    return sum(args)    
# Calling the function with type hints and variable number of arguments
print(add_multiple_numbers_with_type_hints(1, 2, 3, 4, 5))  # Output: 15    
# Function with type hints and keyword arguments
def print_info_with_type_hints(name: str, age: int) -> None:    
    """Function to print name and age with type hints."""
    print(f"Name: {name}, Age: {age}")

# Calling the function with type hints and keyword arguments   
print_info_with_type_hints(name="Alice", age=30)  # Output: Name: Alice, Age: 30 
# Function with type hints and default parameters

def print_info_with_default_and_type_hints(name: str = "Unknown", age: int = 0) -> None:
    """Function to print name and age with default values and type hints."""
    print(f"Name: {name}, Age: {age}")  
# Calling the function with type hints and default parameters
print_info_with_default_and_type_hints()  # Output: Name: Unknown, Age: 0

# Function with type hints and return value
def multiply_with_type_hints(a: int, b: int) -> int:
    """Function to multiply two numbers with type hints."""
    return a * b    
    