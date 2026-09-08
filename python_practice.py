# This is your first coding assignment for Computational BME.
# As discussed in class, feel free to use AI tools to help you complete this assignment, but remember to cite them.
# I encourage you to try the problems yourself first and only use AI tools when you are stuck to benefit your learning. 

# Name: Vincent LaGrua
# Resources: Claude Sonnet 5: Used to review coding topics and build understanding thorugh debugging and hints toward the solution. 

# %% ###########################################################
# Problem 1: Practice writing pseudocode

# Write pseudocode that will input a integer N and output the sum of the first N numbers in the fibonacci sequence.
# Fibonacci sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# Example: If N = 5, the output should be 0 + 1 + 1 + 2 + 3 = 7

""" 

Pseudocode:
Input: N (an integer)
set a to 0 (first Fibonacci number)
set b to 1 (next Fibonacci number)
set total to 0 (keeps track of the sum)
set count to 0 (tracks how many numbers have been added)
set next to 0 (this will be the next Fibonacci number)

While count is less than N 
set the total to total + a 
set next to a + b
set a equal to b
set b equal to next
add one to the count

Output: total 

"""

# %% ###########################################################
# Problem 2: Comment your code
# Comments are very helpful for others (especially when pair-coding!) and yourself to understand your code! Add comments to the following code, which will run but produces the wrong output. Once you comment the code, you should be able to identify the error and fix it (the correct total that should be printed is 12).
N = 6 # Sum the first 6 numbers in the Fibonacci sequence (0+1+1+2+3+5)

a = 0 # set a to the first fibonacci number
b = 1 # set b to the second fibonacci number
count = 0 # start count with zero
total = 0 # adjust total

while count < N: 
    total = total + a   # total should not equal the second Fibonacci number but the first, so I changed b to a 

    next_value = a + b  # the next value in the sequence is the sum of the previous two
    a = b   # the first value now equals the second value
    b = next_value  # the second value now equals the next value

    count = count + 1   # adds one to the count 

print(total) # prints the final sum 

# %% ###########################################################
# Problem 3: Using common Python libraries
# What is the standard deviation of the first 10 numbers in the fibonacci sequence? Use the numpy library to calculate the standard deviation.

# Code for the list
a = 0
b = 1
fib_list = []  # empty list to store the Fibonacci numbers

for i in range(10):  
    fib_list.append(a)  # adds the new number to the list
    next_value = a + b
    a = b
    b = next_value

print(fib_list)

import numpy as np

std_dev = np.std(fib_list)
print(std_dev)

# Standard Deviation = 10.47

# %% ###########################################################
# Problem 4: Don't repeat yourself by writing functions
# Write a function that takes an integer N as input and returns the sum of the first N numbers in the fibonacci sequence.
# Then use this function to calculate the sums for N = 5, 10, 15, 20, 25, and 30 and print them as a list.

def fib_sum(N):
    a, b = 0, 1 # more compact way of storing variables a and b 
    total = 0
    for i in range(N):
        total = total + a
        a, b = b, a + b
    return total

results = [fib_sum(n) for n in [5, 10, 15, 20, 25, 30]]
print(results)

# %% ###########################################################
# Problem 5: Read your error messages
# Run the following code block to see what the error messages are. Then, for each error:
# 1. Identify what type of error it is (SyntaxError, NameError, TypeError, etc.)
# 2. Add a comment to the line that is throwing the error explaining what the error is
# 3. Fix the error so that the code runs correctly

# You will only see one error at a time when you run the code. After fixing one error, run the code again to see the next error. Your final code should work correctly and will have comments where the original errors were.


def find_fib_above_limit(limit):
    """# The function inputs an integer called "limit" and finds the first number that goes above "limit" in the fibonacci sequence. It returns the index of that number.
    :param limit: limit of fibonacci sequence
    :type limit: integer
    :return: index of the first number above limit
    :rtype: integer
    """
    a = 0   # Cause of TypeError: was "0" (a string) which cannot be compared with integers, so changed to 0
    b = 1   # Same issue as with a, changed to integer 1
    index = 0   # Cause of UnboundLocalError: line added to create the variable index

    while a <= limit:   # TypeError: "<=" is not supported between instances of strings and integers
        next_value = a + b
        a = b
        b = next_value
        index += 1  # UnboundLocalError: index is not associated with a value so it cannot be accessed

    return index


result = find_fib_above_limit(50)
print("The index of the first number above your limit is: ", result)

# %% ###########################################################
# Problem 6: Test your code
# The following function will run but will output the wrong answer sometimes. Add test cases to verify that the function works correctly for a variety of inputs. If you find any inputs that produce incorrect outputs, fix the function. The function, when working properly, should return the sum of all odd Fibonacci numbers less than or equal to the input "limit".


def sum_odd_fib(limit):
    a, b = 0, 1
    total = 0
    while b <= limit:
        if b % 2 != 0:  # this line checks if the Fibonacci number is even - fixed to check for ODD numbers instead
            total = total + b   # fixed to account for the cumulative total, total = b only tracked the last value, forgetting everything added before
        a, b = b, a + b
    return total


# Add your test cases here
print(sum_odd_fib(0)) # Expected: 0
print(sum_odd_fib(10)) # Expected: 10   (1+1+3+5)
print(sum_odd_fib(25)) # Expected: 44   (1+1+3+5+13+21)
print(sum_odd_fib(100)) # Expected: 188 (44(previous)+55+89)

# %%
