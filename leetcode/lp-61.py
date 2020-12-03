
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        if not head or not head.next :
            return head

        n=1
        end_tail = head
        while end_tail.next:
            end_tail = end_tail.next
            n+=1

        end_tail.next = head

        front_tail = head

        for _ in range(n-k%n-1):
            front_tail = front_tail.next

        new_head = front_tail.next

        front_tail.next = None

        return new_head

        
