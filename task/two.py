#prgram to check if a string is substring of another string

def substring(main_str, sub_str):
    return sub_str in main_str

main_str = input("Enter the main string: ")
sub_str = input("Enter the string to check: ")

if substring(main_str, sub_str):
    print(f"'{sub_str}' is a substring of '{main_str}'.")
else:
    print(f"'{sub_str}' is not a substring of '{main_str}'.")
