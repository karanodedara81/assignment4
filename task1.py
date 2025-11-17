# Module 5: Files, Exceptions, and Errors in Python
#
# Task 1: Read a File and Handle Errors
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.
try:
    with open('sample.txt', 'r') as file:
        for index , line in enumerate(file,start=1):
            print(f"Line {index} : {line.strip()}")
except FileNotFoundError:
    print("Error : the file 'sample.txt' does not exist")

except Exception as e:
    print(f"error occured: {e}")
