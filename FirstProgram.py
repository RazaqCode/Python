# Reverse a string using a loop

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Example
string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))
