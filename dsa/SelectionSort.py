# Algorithm
def selectionSort(list):
    index = 0
    while index <= len(list) -1:
        minIndex = index
        for i in range(index, len(list)):
            if list[i] < list[minIndex]:
                minIndex = i
        list = list[:index] + [list[minIndex]] + list[index:minIndex] + list[minIndex+1:]
        index += 1

    return list

# Tests
assert(selectionSort([]) == [])
assert(selectionSort([3]) == [3])
assert(selectionSort([1, 2, 3]) == [1, 2, 3])
assert(selectionSort([4, 3, 9, 6, 12, 5]) == [3, 4, 5, 6, 9, 12])
print("Done.")