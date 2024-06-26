"""You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. 
The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order."""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        """dummy = ListNode(0)
        current = dummy
        
        # Traverse both lists simultaneously
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Append remaining nodes from list1 or list2 (if any)
        if list1:
            current.next = list1
        else:
            current.next = list2
        
        # The merged list starts from the next of dummy node
        return dummy.next"""
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        ptr1 = list1
        ptr2 = list2
        if list1.val > list2.val:
            mergedListHead = list2
            ptr2 = ptr2.next
        else:
            mergedListHead = list1
            ptr1 = ptr1.next
        mergedListPtr = mergedListHead
        while ptr1 != None and ptr2 != None:
            if ptr1.val > ptr2.val:
                mergedListPtr.next = ptr2
                ptr2 = ptr2.next
            else:
                mergedListPtr.next = ptr1
                ptr1 = ptr1.next
            mergedListPtr = mergedListPtr.next
        if ptr1 == None:
            mergedListPtr.next = ptr2
        else:
            mergedListPtr.next = ptr1
        return mergedListHead
    

    
test = Solution()
mergeLists = test.mergeTwoLists(list1 = [0], list2 = [1,3,4])
print(mergeLists)