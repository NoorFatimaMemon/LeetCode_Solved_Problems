"""Given two strings ransomNote and magazine, return true 
if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1: Input: ransomNote = "a", magazine = "b", Output: false
Example 2: Input: ransomNote = "aa", magazine = "ab", Output: false
Example 3: Input: ransomNote = "aa", magazine = "aab", Output: true
 
Constraints:
1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """       
        from collections import Counter
        count_ransomNote = Counter(ransomNote)
        count_magazine = Counter(magazine)
        for char, count in count_ransomNote.items():
            if count_magazine[char] < count:
                return False
        
        return True

test = Solution()
output = test.canConstruct(ransomNote = "aa", magazine = "ab")
print(output)