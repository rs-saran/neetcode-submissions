# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        list_length = 0

        p = head

        while p:
            list_length+=1
            p=p.next

        c = 1
        target = (list_length -n + 1)
        
        dummyNode = ListNode()
        prev = dummyNode
        prev.next = head

        while c<= target and prev.next:
            print(c, target, prev.next.val, end = ' ')

            if c == target:
                prev.next = prev.next.next
                print("eq")

            else:
                prev = prev.next
                print()
                
            c+=1
        
        return dummyNode.next
        

            






        