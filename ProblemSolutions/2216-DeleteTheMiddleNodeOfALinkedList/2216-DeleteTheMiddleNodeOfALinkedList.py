# Last updated: 7/18/2025, 10:57:04 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def count_nodes(head):

            if head is None:
                return 0

            return 1 + count_nodes(head.next)

        def remove_middle_value(head, index):
            if index == 0:
                return head.next

            i = 0
            current = head

            while current:
                if index - 1 == i:
                    # we dont need to validate .next.next because its on the middle
                    current.next = current.next.next
                    break

                current = current.next

                i += 1

            return head

        n = count_nodes(head)
        middel_index = n // 2
        result = remove_middle_value(head, middel_index)

        return result