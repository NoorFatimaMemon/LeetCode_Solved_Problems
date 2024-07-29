"""Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists."""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        desired_output_lst = []
        for index1, number1 in enumerate(nums):
            indx = index1+1
            for index2 in range(indx, len(nums)):
                number2 = nums[index2]
                output = int(number1 + number2)
                if output == target:
                    desired_output_lst.append(index1)
                    desired_output_lst.append(index2)

        return desired_output_lst
test = Solution()
desired_output_lst = test.twoSum(nums=[3,3], target=6)
print(desired_output_lst)