"""A perfect number is a positive integer that is equal to the sum of its positive divisors, 
excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.
Given an integer n, return true if n is a perfect number, otherwise return false.

Example 1: Input: num = 28, Output: true, 
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.

Example 2: Input: num = 7, Output: false

Constraints: 1 <= num <= 108"""

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        """if 1 <= num <= pow(10, 8):
            divisors = sorted([factor for factor in range(1, num+1) if num%factor == 0])
            divisors.pop(-1)
            Sum = sum(divisors) 
            if Sum==num: return True
            else: return False 
        else: return False """

        import math
        if num <= 1:
            return False
        
        total_sum = 1
        sqrt_num = int(math.sqrt(num))
        
        for i in range(2, sqrt_num + 1):
            if num % i == 0:
                total_sum += i
                if i != num // i:
                    total_sum += num // i
        
        return total_sum == num

test = Solution()
output = test.checkPerfectNumber(28)
print(output)