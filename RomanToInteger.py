# Solution
def romanToInt(s: str) -> int:
    i = 0
    val = 0
    finished = False
    while not finished:
        symbol = s[i]
        nextSymbol = ""
        if i+1 != len(s):
            nextSymbol = s[i+1]
        if symbol == "I" and (nextSymbol == "V" or nextSymbol == "X"):
            val += 4 if nextSymbol == "V" else 9
            i += 1
        elif symbol == "X" and (nextSymbol == "L" or nextSymbol == "C"):
            val += 40 if nextSymbol == "L" else 90
            i += 1
        elif symbol == "C" and (nextSymbol == "D" or nextSymbol == "M"):
            val += 400 if nextSymbol == "D" else 900
            i += 1
        else:
            if (symbol == "M"): val += 1000
            elif (symbol == "D"): val += 500
            elif (symbol == "C"): val += 100
            elif (symbol == "L"): val += 50
            elif (symbol == "X"): val += 10
            elif (symbol == "V"): val += 5
            elif (symbol == "I"): val += 1
        i += 1
        if i >= len(s): finished = True

    return val

# Tests
assert romanToInt("III") == 3
assert romanToInt("IV") == 4        