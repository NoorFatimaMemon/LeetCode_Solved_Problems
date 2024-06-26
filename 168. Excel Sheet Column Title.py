"""Given an integer columnNumber, return its corresponding column title as it appears in an 
Excel sheet.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
Example 1: Input: columnNumber = 1, Output: "A"
Example 2: Input: columnNumber = 28, Output: "AB"
Example 3: Input: columnNumber = 701, Output: "ZY"
Constraints: 1 <= columnNumber <= 231 - 1"""

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        import string
        alpha_dict = {index + 1: char  for index, char in enumerate(list(string.ascii_uppercase))}
        #alpha = [chr(i) for i in range(ord('A'),ord('Z')+1)]
        result = ''
        while columnNumber > 0:
            result += alpha_dict[(columnNumber-1) % 26 + 1]
            columnNumber = int((columnNumber-1) // 26)
        return result[::-1]
                
test = Solution()
output = test.convertToTitle(27)
print(output)