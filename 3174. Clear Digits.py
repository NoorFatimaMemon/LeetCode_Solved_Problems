"""You are given a string s. Your task is to remove all digits by doing this operation repeatedly:
Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Example 1: Input: s = "abc", Output: "abc"
Explanation: There is no digit in the string.

Example 2: Input: s = "cb34", Output: "", 
Explanation: First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".

Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits."""

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        if 1 <= len(s) <= 100:
            s_list = list(s)
            indx = 0
            while indx < len(s_list):
                if s_list[indx].isdigit() and not s_list[indx-1].isdigit():
                    s_list.pop(indx)
                    s_list.pop(indx-1)
                    indx = 0
                else: indx += 1
            return ''.join(s_list)            

test = Solution()
output = test.clearDigits("abc77c")
print(output)