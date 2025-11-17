# Task 2: Write and Append Data to a File
#
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

text_to_write = input("enter text to write: ")
with open("output.txt", "w") as file:
    file.write(text_to_write + "\n")

print("data successfully written to output.txt")

text_to_append = input("Enter additional text to append to the file : ")
with open("output.txt", "a") as file:
    file.write(text_to_append + "\n")

print("Additional data appended to output.txt")

print("\nFinal content of output.txt : ")
with open("output.txt", "r") as file:
    content = file.read()
    print(content)