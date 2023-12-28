# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q=[]
        temp=head
        curr=ListNode()
        while(temp!=None):
            q.append(temp)
            temp=temp.next
        while len(q)>1:
            first,last=q.pop(0),q.pop()
            curr.next=first
            first.next=last
            curr=last
        if q:
            curr.next=q.pop()
            curr=curr.next
        curr.next=None
        return curr.next
            

