# Solution
def isPalindrome(x: int) -> bool:
    if (x >= 0):
        strX = str(x)
        for i in range(0, len(strX) // 2):
            if (strX[i] != strX[-(i+1)]):
                return False
    else:
        return False
    return True

# Tests
assert isPalindrome(323) == True
assert isPalindrome(1) == True
assert isPalindrome(0) == True
assert isPalindrome(224535422) == True
assert isPalindrome(-121) == False
assert isPalindrome(998) == False
assert isPalindrome(77557) == False