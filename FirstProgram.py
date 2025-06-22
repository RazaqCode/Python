# Reverse a string using recursion

def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

# Example
string = input("Enter a string: ")
print("Reversed string:", reverse_string(string))
