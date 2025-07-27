# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            new_digit = total_sum % 10

            current.next = ListNode(new_digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next

# Helper to create linked lists from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

# Helper to convert linked list to a list for printing
def linked_list_to_list(node):
    arr = []
    while node:
        arr.append(node.val)
        node = node.next
    return arr

# Test Cases
l1 = create_linked_list([2,4,3]) # Represents 342
l2 = create_linked_list([5,6,4]) # Represents 465
result = Solution().addTwoNumbers(l1, l2)
print(f"Add Two Numbers (342 + 465): {linked_list_to_list(result)}") # Expected: [7, 0, 8]

l1 = create_linked_list([0])
l2 = create_linked_list([0])
result = Solution().addTwoNumbers(l1, l2)
print(f"Add Two Numbers (0 + 0): {linked_list_to_list(result)}") # Expected: [0]

l1 = create_linked_list([9,9,9,9,9,9,9])
l2 = create_linked_list([9,9,9,9])
result = Solution().addTwoNumbers(l1, l2)
print(f"Add Two Numbers (9999999 + 9999): {linked_list_to_list(result)}") # Expected: [8, 9, 9, 9, 0, 0, 0, 1]