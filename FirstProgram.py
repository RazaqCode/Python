text = input("Enter text: ").lower()
vowels = "aeiou"
count = sum(1 for char in text if char in vowels)
print("Number of vowels:", count)
