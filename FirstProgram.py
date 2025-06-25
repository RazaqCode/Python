# Numeric Types
int_var = 10
float_var = 3.14
complex_var = 2 + 3j

# Text Type
str_var = "Hello, Python!"

# Sequence Types
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
range_var = range(5)

# Set Types
set_var = {7, 8, 9}
frozenset_var = frozenset([10, 11, 12])

# Mapping Type
dict_var = {"name": "Razaq", "role": "Developer"}

# Boolean Type
bool_var = True

# Binary Types
bytes_var = b"Hello"
bytearray_var = bytearray(3)
memoryview_var = memoryview(bytes(5))

# None Type
none_var = None

# Print value and its data type
variables = [
    int_var, float_var, complex_var, str_var,
    list_var, tuple_var, range_var,
    set_var, frozenset_var, dict_var,
    bool_var, bytes_var, bytearray_var, memoryview_var,
    none_var
]

for var in variables:
    print(f"Value: {var} | Type: {type(var)}")
