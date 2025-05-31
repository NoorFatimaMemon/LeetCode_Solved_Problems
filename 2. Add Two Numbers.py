"""You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:
The number of nodes in each linked list is in the range [1, 100]. 0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros."""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        carry = 0
        num1 = l1
        num2 = l2
        dummy = ListNode()
        out = dummy

        while num1 or num2:
            val1 = num1.val if num1 else 0
            val2 = num2.val if num2 else 0
            sum = carry + val1 + val2
            if sum < 10:
                out.next = ListNode(sum)
                carry = 0
            else:
                out.next = ListNode(sum % 10)
                carry = sum//10
                sum = 0
             
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next

            out = out.next
        
        if carry:
            out.next =  ListNode(carry)
        
        return dummy.next