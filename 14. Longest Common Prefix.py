"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters."""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""

        base = strs[0]
        for index in range(len(base)):
            for word in strs[1:]:
                if index == len(word) or word[index] != base[index]:
                    return base[0:index]

        return base
    
test = Solution()
longest_Common_Prefix = test.longestCommonPrefix(["flower","flow","flight"])
print(longest_Common_Prefix)
