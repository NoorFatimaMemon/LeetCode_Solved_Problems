"""Given an integer array nums, move all 0's to the end of it while maintaining the relative 
order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1: Input: nums = [0,1,0,3,12], Output: [1,3,12,0,0]
Example 2: Input: nums = [0], Output: [0]

Constraints: 1 <= nums.length <= 104, -231 <= nums[i] <= 231 - 1"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: nums[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        for idx in range(len(nums)):
            if nums[idx] != 0:
                nums[count], nums[idx] = nums[idx], nums[count]
                count+=1
        return nums

test = Solution()
output = test.moveZeroes([0])
print(output)