"""Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1: Input: x = 123, Output: 321
Example 2: Input: x = -123, Output: -321
Example 3: Input: x = 120, Output: 21

Constraints: -2^31 <= x <= 2^31 - 1"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        minimum_value, maximum_value = -2**31, 2**31 - 1
        is_negative, x, output  = x < 0, abs(x), 0 
        while x != 0:
            digit = x % 10
            x //= 10
            if (output > (maximum_value - digit) // 10):
                return 0
            output = output * 10 + digit
        
        if is_negative: output = -output
        if output < minimum_value or output > maximum_value: return 0

        return output      

test = Solution()
output = test.reverse(1534236469)
print(output)