def factorial(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integer')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integer')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(10)
print(result)

def factorialWithSpace(n):
    space = ' ' * (4 * n)
    print(space,'factorial',n)
    if n == 0:
        print(space, 'returning 1')
        return 1 
    else:
        recurse = factorialWithSpace(n-1)
        result = recurse * n
        print(space,'returning', result)
        return result
factorialWithSpace(4)
