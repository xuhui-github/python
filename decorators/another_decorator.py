def another_function(func):
    """
    A function that accept another another_function
    """

    def other_func():
        val = "the result of %s is %s" % ( func(), eval(func()))
        return val
    return other_func

@another_function
def a_function():
    """A pretty useless function"""
    return "1+1"

if __name__ == "__main__":
    value = a_function()
    print(value)
