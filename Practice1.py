# If - else comprehension

age = 20
status = "Adult" if age >= 20 else "Teenager" if all((age > 13, age < 20)) else "Minor" if all((age > 5, age < 13)) else "Invalid Age!"
print(status,"\n")

# List Comprehension
squares = [i**2 for i in range(1, 11)]
print(squares,"\n")

# Dictionary Comprehension
squares_dict = {i: i**2 for i in range(1,11)}
print(squares_dict,"\n")

# Enumerate - helps us to get index of element in a list quickly
fruits = ['Apple', 'Banana', 'Orange', 'Fruit']
for index, fruit in enumerate(fruits):
    print(index+1, fruit)
print()


# Swapping Variables
a, b = 5, 10
print(a, b)
a, b = b, a
print(a, b, "\n")

# Using counter - quickly counts the frequency of elements
from collections import Counter
words = ['apple', 'banana', 'apple', 'orange',
         'pomegranate', 'watermelon', 'orange', 'apple']
counter = Counter(words)
print(counter, "\n")

# Combining Lists with zip
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]
combined = list(zip(names, scores))
print(combined, "\n")

# String Reversal
text = "Python"
reversed_text = text[::-1]
print(reversed_text, "\n")

# Merging Dictionary - basically the 2nd dictionary overwrites the 1st dictionary
dict1 = {'a': 1, 'b': 10}
dict2 = {'b': 3, 'c': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict, "\n")

# Reading a text file
with open('story.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    for text in lines:
        if text == '':
            lines.remove(text)
print(lines)


