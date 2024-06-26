"""Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it

Example 1: Input: numRows = 5, Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2: Input: numRows = 1, Output: [[1]]
Constraints: 1 <= numRows <= 30"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        
        output_list = [[1]]
        for row in range(1, numRows):
            previous_row = output_list[-1]
            new_row = [1]  # First element is always 1
            
            for j in range(1, row):
                new_row.append(previous_row[j - 1] + previous_row[j])  # Middle elements are sum of adjacent elements
                
            new_row.append(1)  # Last element is always 1
            output_list.append(new_row)       
            
        return output_list
            
test = Solution()
output = test.generate(5)
print(output)
        