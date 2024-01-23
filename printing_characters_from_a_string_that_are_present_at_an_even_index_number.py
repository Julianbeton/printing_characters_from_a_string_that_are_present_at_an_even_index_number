# Exercise 3: Print characters from a string that are present at an even index number

# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

# Expected Output: Orginal String is  pynative
# Printing only even index chars
# p
# n
# t
# v

# pseudocode
# input word
word = input("Enter a valid word  ")

# print original string
print("Original String:", word)

# print what program run
print(" Printing only even index characters")

length_of_the_word = len(word)
# range for word
for i in range(0, length_of_the_word, 2):
    print(word[i])