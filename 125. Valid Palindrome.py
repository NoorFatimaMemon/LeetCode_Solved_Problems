"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
 
Constraints: 1 <= s.length <= 2 * 105, s consists only of printable ASCII characters."""


class Solution(object):
    def isPalindrome(self, s):
        if s == '' or s == " ":
            return True

        import re
        s = s.lower()
        test_str = re.sub(r'[^a-zA-Z0-9]', '', s) #re.sub(r'\W+', '', s) doesnot remove underscores
        reversed_value = test_str[::-1]
        print(reversed_value)
        if test_str == reversed_value:
            return True
        else:
            return False
        
test = Solution()
Output = test.isPalindrome("A man, a plan, a canal: Panama")
print(Output)