
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse_ls(self, cur):
        prev = None
        while cur and cur.next:
            temp = cur.next
            cur.next = prev

            prev = cur
            cur = temp
        cur.next = prev
        return cur

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # reverse half
        ptr2=self.reverse_ls(slow.next)
        slow.next=None

        ptr1 = head
        while ptr1.next and ptr2.next:
            temp1 = ptr1.next
            temp2 = ptr2.next

            ptr1.next = ptr2
            ptr2.next = temp1

            ptr1 = temp1
            ptr2 = temp2
        if ptr1.next:
            temp= ptr1.next
            ptr1.next=ptr2
            ptr1.next.next=temp
        else:
            ptr1.next=ptr2
