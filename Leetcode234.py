# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self,cur):
        prev=None
        while cur and cur.next:
            temp=cur.next
            cur.next=prev

            prev=cur
            cur=temp
        cur.next=prev
        return cur


    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head.next or not head:
            return True 

        fast=head
        slow=head
        while fast.next and fast.next.next:
            fast=fast.next.next
            slow=slow.next
        
        # reverse 
        reversed_ls=self.reverse(slow.next)

        ptr=head
        # compare
        while reversed_ls and ptr:
            if reversed_ls.val != ptr.val:
                return False
            reversed_ls=reversed_ls.next
            ptr=ptr.next
        return True
            
