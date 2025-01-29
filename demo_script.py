# Python Workshop Examples
# Topics covered: variables, data types, functions, loops, lists, and basic operations

import random

# 1. Variables and Basic Data Types
name = "Alice"
age = 25
height = 1.75
is_student = True

print("--- Basic Variables Example ---")
print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Height: {height} (Type: {type(height)})")
print(f"Is Student?: {is_student} (Type: {type(is_student)})")

# 2. Functions
def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle
    Returns:
        float: The area of the rectangle
    """
    return length * width

print("\n--- Functions Example ---")
length = 5
width = 3
area = calculate_rectangle_area(length, width)
print(f"Rectangle area (length={length}, width={width}): {area}")


# # 3. Lists and Loops (Original version)
# def find_even_numbers(numbers):
#     """
#     Find all even numbers in a list.
#     Args:
#         numbers (list): List of integers
#     Returns:
#         list: List containing only even numbers
#     """
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers

# print("\n--- Lists and Loops Example ---")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(f"Original list: {numbers}")
# print(f"Even numbers: {find_even_numbers(numbers)}")

# 3. Lists and Loops (Improve version)
def find_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    even_count = len(even_numbers)
    return even_numbers, even_count

# Example usage:
print("\n--- Lists and Loops Example ---")
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Generate a list of 10 random numbers between 1 and 1000
numbers = [random.randint(0, 100) for _ in range(100)]

even_numbers, even_count = find_even_numbers(numbers)
print(f"Original list: {numbers}")
print(f"Even numbers: {even_numbers}")
print(f"Count of even numbers: {even_count}")


# 4. String Manipulation
def count_vowels(text):
    """
    Count the number of vowels in a string.
    Args:
        text (str): Input string
    Returns:
        int: Number of vowels
    """
    vowels = 'aeiou'
    return sum(1 for char in text.lower() if char in vowels)

print("\n--- String Manipulation Example ---")
sample_text = "Hello Python Workshop!"
print(f"Text: {sample_text}")
print(f"Number of vowels: {count_vowels(sample_text)}")

# 5. Dictionary Example
def create_word_frequency(sentence):
    """
    Create a dictionary of word frequencies.
    Args:
        sentence (str): Input sentence
    Returns:
        dict: Dictionary with word frequencies
    """
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

print("\n--- Dictionary Example ---")
sentence = "the quick brown fox jumps over the lazy dog"
print(f"Sentence: {sentence}")
print(f"Word frequency: {create_word_frequency(sentence)}")
