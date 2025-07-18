# Last updated: 7/18/2025, 10:57:19 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        even_head = head.next

        odd = head  # odd
        even = head.next  # even

        while odd and odd.next and even and even.next:

            odd.next = odd.next.next
            odd = odd.next

            if even.next:
                even.next = even.next.next
                even = even.next
        else:
            odd.next = even_head

        return head