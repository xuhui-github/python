def palindrome(s):
    if s == "":
        return True
    elif len(s) == 1:
        return True
    else:
        return s[0] == s[-1] and palindrome(s[1:-1])


print(palindrome("abcde"))
print(palindrome("abcba"))
print(palindrome("123321"))
print(palindrome("我是我"))
