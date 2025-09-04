# Last updated: 7/21/2025, 8:32:44 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        max_value = -1

        # we find first half of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # we got the second have that needs to be reversed
        current = slow
        previous = None
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        # previous holds the reversed elements
        current = previous
        head_current = head
        while current:
            summed = head_current.val + current.val
            if summed > max_value:
                max_value = summed
            current = current.next
            head_current = head_current.next

        return max_value