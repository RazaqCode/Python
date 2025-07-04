print("8. Generators")
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

for num in count_up_to(3):
    print("Yielded:", num)
print()