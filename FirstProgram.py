num = int(input("Enter a number: "))

# Convert to string and check if same when reversed
if str(num) == str(num)[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
