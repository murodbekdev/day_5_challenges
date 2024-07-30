
import random
'''
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:  # via for loop
    print(fruit)
    print(fruit + " Pie")    # goes into each value of fruits list and adds Pie word
    # and indentation is very important which means when we declare a bunch of code we need to notice the indentation
    #print(fruits)
    """
       The outcome is like: Apple
       Apple Pie
       ['Apple', 'Peach', 'Pear']
       Peach
       Peach Pie
       ['Apple', 'Peach', 'Pear']
       Pear
       Pear Pie
       ['Apple', 'Peach', 'Pear']
       
    """

# if i use this print function out of for loop it looks like that


print(fruits)
'''
"""
Apple
Apple Pie
Peach
Peach Pie
Pear
Pear Pie
['Apple', 'Peach', 'Pear']  So indentation is so much important 
"""


'''
# Average Height Calculator

student_heights = input("Input a list of student heights ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# we have sum() and len() built-in-functions functions that are always available
# in Python without needing to import any additional modules. But the challenges requires not to use them at all

total_height = 0
for height in student_heights:
    total_height += height


number_of_students = 0

for student in student_heights:
    number_of_students += 1


average_height = round(total_height / number_of_students)
print(average_height) 

'''
'''
student_scores = input("Input a list of student heights ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


max_scores = 0 # # or equal to 0 # Start with the first element as the initial maximum

for score in student_scores:  # using for loop score into student_scores
    if score > max_scores:  #  such as [5, 6, 7, 8, 9] and we take the first element as 5 if each score is greater than other
        max_scores = score   # then, it will be our max_scores
print(f"The maximum value is: {max_scores}")


# number_of_students = 0
#
# for student in student_heights:
#     number_of_students += 1
#
#
# average_height = round(total_height / number_of_students)
# print(average_height)

'''

'''
# For Loop with Range
for number in range(0, 101, 2):
    number = number + 2
    print(number)


# If we want to accumulate the total number we can declare new variable called total equal to 0
total = 0
for number in range(0, 101, 2):
    total += number
print(total)   # is equal to 5050 we can calcualte any number in total

# Alternatively, we can do another option like
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)   # We got the same result. So, whatever you like 

'''


# FizzBuzz challnege




number = int(input("Please insert the number between 0 and 100: "))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("Others can not be dived both 3 and 5")
# I am done the challenge

letters = ['A', 'b', 'C', 'd', 'E', 'f', 'G', 'h', 'I', 'j', 'K', 'l', 'M', 'n', 'O', 'p', 'Q', 'r', 'S', 't', 'U', 'v', 'W', 'x', 'Y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '?']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your passsword? \n"))
nr_symbols = int(input("How many symbols would you like? \n"))
nr_numbers = int(input("How many numbers would you like? \n"))
'''
password = ""  # empty string

for char in range(1, nr_letters + 1):
    password += random.choice(letters)  # random.choice method in Python is used to select a random element from a non-empty sequence such as a list, tuple, or string.

for char in range(1, nr_symbols + 1):# why we increase to 1 because in range nr_symbols entering int is not included, so adding to 1 is mandatory
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)
'''
# Hard one

password_list = []  # doing empty list

for char in range(1, nr_letters + 1):
    password_list += random.choice(letters)  # random.choice method in Python is used to select a random element from a non-empty sequence such as a list, tuple, or string.

for char in range(1, nr_symbols + 1):# why we increase to 1 because in range nr_symbols entering int is not included, so adding to 1 is mandatory
    password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)
print(password_list)   # ordered in the list
random.shuffle(password_list)  # function in Python is used to randomly shuffle the elements of a list in place, meaning the original list is modified and no new list is created (reorderder other mean of this function)
print(password_list)  # here we got just a list shuffled : reordered in the list

password = ""    # here we can get generated password from the list to convert it final password
for char in password_list:
    password += char
print(f"Your passsword is: {password}")