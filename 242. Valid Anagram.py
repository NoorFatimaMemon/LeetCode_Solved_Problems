"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1: Input: s = "anagram", t = "nagaram", Output: true
Example 2: Input: s = "rat", t = "car", Output: false

Constraints: 1 <= s.length, t.length <= 5 * 104, s and t consist of lowercase English letters.
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        s, t = sorted(s), sorted(t)
        for index in range(len(s)):
            if s[index] != t[index]:
                return False
        return True
        
test = Solution()
output = test.isAnagram(s = "aacc", t = "ccac")
print(output)