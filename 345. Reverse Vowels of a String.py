"""Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1: Input: s = "hello", Output: "holle"
Example 2: Input: s = "leetcode", Output: "leotcede"

Constraints: 1 <= s.length <= 3 * 105, s consist of printable ASCII characters."""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        Vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'] 
        s = list(s)
        i, j = 0, len(s)-1
        while(i<j):
            if s[i] not in Vowels:
                i += 1
            elif s[j] not in Vowels:
                j -= 1
            else:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)
    
test = Solution()
output = test.reverseVowels(s = "adios")
print(output)