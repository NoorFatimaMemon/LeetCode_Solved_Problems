"""You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
Example 1: Input: n = 5, Output: 2, Explanation: Because the 3rd row is incomplete, we return 2.
Example 2: Input: n = 8, Output: 3, Explanation: Because the 4th row is incomplete, we return 3.
 
Constraints:
1 <= n <= 231 - 1"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        number_of_rows = 0
        for indx in range(1, n+1):
            if indx <= n:
                number_of_rows += 1                
                n -= indx    
            else:
                return number_of_rows
        return number_of_rows
        # or use return int((math.sqrt(1 + 8 * n) - 1) // 2) b/c 2k(k+1) ≤n

test = Solution()
desired_output = test.arrangeCoins(8)
print(desired_output)