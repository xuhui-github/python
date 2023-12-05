def isPower( a , b):
    if a < b:
        return False
    elif a == b:
        return True
    else:
        return isPower(a/b, b)


print(isPower(1,2))
print(isPower(3,2))

def gcd(a, b):
    if a%b == 0:
        return b
    return gcd(b, a%b)
print(gcd(20,4))
