# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
             head
        None <- 1 <- 2 <- 3 <- 4 -> None
                              prev cur next
             head
        None <- 1 <- 2 <- 3 <- 4 None
                             prev  
                                   cur
                                   next
        None <- 1 <- 2 <- 3  None
                        prev
                             cur
                             next

        while cur
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev
        '''
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        return prev