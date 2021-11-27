# Solution
def binarySearch(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


# Tests
assert(binarySearch([], 2) == None)
assert(binarySearch([3], 3) == 0)
assert(binarySearch([1, 2, 3], 3) == 2)