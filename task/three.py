# count frequency of character in a string
def count_frequency(str):
    frequency={}
    for char in str:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

input_str = input("Enter a string: ")

frequency = count_frequency(input_str)

print("Character frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")