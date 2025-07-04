print("3. *args and **kwargs")
def example_func(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

example_func(1, 2, 3, name="Razaq", role="Developer")
print()