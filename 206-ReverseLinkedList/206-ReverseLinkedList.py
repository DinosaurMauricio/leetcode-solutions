# Last updated: 7/20/2025, 3:02:53 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(reverse_head):

            if not head or reverse_head.next is None:
                return reverse_head

            start_head = reverse(reverse_head.next)

            # have to break link to other nodes
            reverse_head.next = None

            current = start_head

            # instead of this saw in leetcode
            # i cuold literally reversed which could have been much better
            # head.next.next = head
            # and reduce to O(N)
            # the other solution was iteratively with two pointers
            # one with the previous and current and holding the next value
            # in a temporary var
            
            while current.next:
                current = current.next

            current.next = reverse_head

            return start_head

        result = reverse(head)

        return result
