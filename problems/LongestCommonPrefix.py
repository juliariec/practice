# Solution
def longestCommonPrefix(strs) -> str:
		listLength = len(strs)
		
		if (listLength == 0):
				return ""
		elif (listLength == 1):
				return strs[0]
		else:
				result = ""
				shortestWord = strs[0]
				
				for i in range(0, listLength):
						if len(strs[i]) < len(shortestWord):
								shortestWord = strs[i]
				
				for strIdx in range(0, len(shortestWord)):
						for wordIdx in range(0, listLength):
								if (strs[wordIdx][strIdx] != shortestWord[strIdx]):
										return result
						result += shortestWord[strIdx]
						
				return result
        

# Tests
assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
assert longestCommonPrefix([]) == ""
assert longestCommonPrefix(["ab", "a"]) == "a"
assert longestCommonPrefix(["yes", "no", "maybe"]) == ""
assert longestCommonPrefix(["jack", "jane", "jill"]) == "j"
assert longestCommonPrefix(["flower", "flower", "flower"]) == "flower"
