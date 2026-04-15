# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 길이가 0이거나 1인 경우 순환이 존재할 수 없으므로 바로 리턴
        if not head or not head.next:
            return False

        slow = head
        fast = head

        while fast and fast.next and slow.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

            
        return False