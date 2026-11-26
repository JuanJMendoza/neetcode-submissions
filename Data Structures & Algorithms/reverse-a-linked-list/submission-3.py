# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
            <- 1 <- 2 <- 3 <- 4
          N      
        '''
        def helper(prev, curr):
            if not curr.next:
                curr.next = prev
                return curr # 4
            
            next_node = helper(curr, curr.next) # 4
            curr.next = prev
            return next_node
        if not head:
            return head
        return helper(None, head)