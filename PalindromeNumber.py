# Solution
def isPalindrome(x: int) -> bool:
    valid = True
    if (x >= 0):
        strX = str(x)
        for i in range(0, len(strX)//2+1):
            if (strX[i] != strX[-(i+1)]):
                valid = False
    else:
        valid = False
    return valid

# Tests
assert isPalindrome(323) == True
assert isPalindrome(1) == True
assert isPalindrome(0) == True
assert isPalindrome(-121) == False
assert isPalindrome(998) == False
assert isPalindrome(77557) == False