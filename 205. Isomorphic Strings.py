"""Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1: Input: s = "egg", t = "add", Output: true
Example 2: Input: s = "foo", t = "bar", Output: false
Example 3: Input: s = "paper", t = "title", Output: true

Constraints:
1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character."""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
           return False 
        
         # Dictionaries to hold mappings
        map_s_to_t = {}
        map_t_to_s = {}
        
        for char_s, char_t in zip(s, t):
            # Check if the current character in s is already mapped to a character in t
            if char_s in map_s_to_t:
                if map_s_to_t[char_s] != char_t:
                    return False
            else:
                map_s_to_t[char_s] = char_t
            
            # Check if the current character in t is already mapped to a character in s
            if char_t in map_t_to_s:
                if map_t_to_s[char_t] != char_s:
                    return False
            else:
                map_t_to_s[char_t] = char_s
        
        return True


test = Solution()
output = test.isIsomorphic("egg", "foo")
print(output)
