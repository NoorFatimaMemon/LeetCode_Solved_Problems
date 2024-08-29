"""Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1: Input: nums = [1,2,3], Output: 6
Example 2: Input: nums = [1,2,3,4], Output: 24
Example 3: Input: nums = [-1,-2,-3], Output: -6

Constraints: 3 <= nums.length <= 104, -1000 <= nums[i] <= 1000"""

class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums, n = sorted(nums, reverse=True), len(nums)
        min_1, min_2, max_1, max_2, max_3 = nums[n-1], nums[n-2], nums[0], nums[1], nums[2]        
        return max(min_1*min_2*max_1, max_1*max_2*max_3)
       

test = Solution()
output = test.maximumProduct([-100,-98,-1,2,3,4])
print(output)