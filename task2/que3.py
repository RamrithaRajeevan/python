#program to print all vowels in a given string, but skip printing if char is space using continue statement

def print_vowels(str):
    vowels = "aeiouAEIOU"
    for char in str:
        if char == ' ':
            continue
        if char in vowels:
            print(char)

str = input("Enter a string: ")
print_vowels(str)
