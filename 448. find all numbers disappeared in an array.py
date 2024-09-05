"""Given an array nums of n integers where nums[i] is in the range [1, n], 
return an array of all the integers in the range [1, n] that do not appear in nums.

Example 1: Input: nums = [4,3,2,7,8,2,3,1], Output: [5,6]
Example 2: Input: nums = [1,1], Output: [2]

Constraints: n == nums.length, 1 <= n <= 105, 1 <= nums[i] <= n"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for idx in range(len(nums)):
            actual_index = abs(nums[idx]) - 1
            nums[actual_index] = abs(nums[actual_index])*(-1)
        
        result = []
        for indx in range(len(nums)):
            if nums[indx] > 0:
                result.append(indx+1)
        
        return result

test = Solution()
output = test.findDisappearedNumbers([1,1])
print(output)