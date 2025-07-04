print("10. Exception Handling")
try:
    value = 10 / 0
except ZeroDivisionError as e:
    print("Caught an exception:", e)
finally:
    print("This block always executes")