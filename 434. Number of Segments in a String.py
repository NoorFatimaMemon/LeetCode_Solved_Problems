"""Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Example 1: Input: s = "Hello, my name is John", Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2: Input: s = "Hello", Output: 1

Constraints: 0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '."""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        """words = s.split(" ")
        segment = 0
        for word in words:
            if word != " " and word != '':
                segment += 1
        return segment  """    
        return len(s.split())  

test = Solution()
output = test.countSegments(s="")
print(output)