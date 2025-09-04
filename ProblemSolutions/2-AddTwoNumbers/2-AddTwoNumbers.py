# Last updated: 7/1/2025, 12:33:22 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = False
        dummy_first = True
        head = None
        tail = None

        while l1 is not None or l2 is not None:
            current_value_1 = l1.val if l1 else "None"
            current_value_2 = l2.val if l2 else "None"

            if l1 and l2:
                value_sum = current_value_1 + current_value_2
            elif l1 and not l2: 
                value_sum = current_value_1
            else:
                value_sum = current_value_2

            #print(f'value sum is {value_sum}')

            if carry:
                value_sum+=1
                carry = False

            value = value_sum % 10 
            carry = value_sum // 10 == 1


            if not head:
                head = ListNode(value)
                tail = head
                
            else:
                tail.next = ListNode(value)
                tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            tail.next = ListNode(1)


        return head






