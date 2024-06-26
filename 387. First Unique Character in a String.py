"""Given a string s, find the first non-repeating character in it and return its index. 
If it does not exist, return -1.

Example 1: Input: s = "leetcode", Output: 0
Example 2: Input: s = "loveleetcode", Output: 2
Example 3: Input: s = "aabb", Output: -1

Constraints: 1 <= s.length <= 105, s consists of only lowercase English letters."""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        precious_char = ''
        for index, char in enumerate(s):
            if precious_char != char:
                char_count = s.count(char)
                if char_count == 1:
                    return index
                else:
                    pass
                precious_char = char
        return -1
                       
test = Solution()
output = test.firstUniqChar("aabb")
print(output)