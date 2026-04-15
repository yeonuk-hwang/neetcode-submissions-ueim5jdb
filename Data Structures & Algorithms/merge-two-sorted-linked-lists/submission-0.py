# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Create a dummy node to act as the starting anchor.
        # This avoids the need for special logic to set the 'head'.
        dummy = ListNode(0)
        current_merged = dummy

        # 2. Iterate as long as both lists have nodes to compare.
        while list1 and list2:
            if list1.val <= list2.val:
                # Redirect the 'next' pointer of our merged list to list1's node
                current_merged.next = list1
                # Advance the pointer in list1
                list1 = list1.next
            else:
                # Redirect the 'next' pointer to list2's node
                current_merged.next = list2
                # Advance the pointer in list2
                list2 = list2.next
            
            # Advance the merged list pointer to the node we just added
            current_merged = current_merged.next

        # 3. Handle the 'residue'.
        # Since the lists are already sorted, if one list ends, we simply 
        # point the tail of our merged list to the remainder of the other list.
        current_merged.next = list1 if list1 is not None else list2

        # The actual head of the merged list is the node after the dummy.
        return dummy.next