try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("the exception argument were", e.args)
