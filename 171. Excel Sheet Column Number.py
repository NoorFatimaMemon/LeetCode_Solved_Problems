"""Given a string columnTitle that represents the column title as appears in an Excel sheet, 
return its corresponding column number.

For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1: Input: columnTitle = "A", Output: 1
Example 2: Input: columnTitle = "AB", Output: 28
Example 3: Input: columnTitle = "ZY", Output: 701
 
Constraints:
1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"]."""

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        import string
        alpha_dict = {char: index + 1 for index, char in enumerate(list(string.ascii_uppercase))}
        """count = 1   
        for char in list(string.ascii_uppercase):
            alpha_dict[char] = count
            count+=1"""

        if len(columnTitle) == 1:
            return alpha_dict[columnTitle]
        else:
            result = 0
            for char in columnTitle:
                result = result * 26 + alpha_dict[char]
            return result

            """power = 0
            sum = 0
            for char in columnTitle[::-1]:
                value = alpha_dict[char] * (26**power)
                power += 1
                sum += value
            return sum"""
                
test = Solution()
output = test.titleToNumber("AB")
print(output)