# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        
        

        if not list1:
            return list2
        else:
            if not list2:
                return list1
            # else:
            #     while list1.val

        l1p = list1
        l2p = list2
        res = None
        prev = None
        c = 1

        while l1p and l2p:
            print(l1p.val,l2p.val,end=" ")
            if l1p.val <= l2p.val:
                if c==1:
                    res = l1p
                    prev = res
                    c+=1
                    l1p=l1p.next
                    print("[",res.val,"]")
                    continue
                prev.next = l1p
                prev =l1p
                l1p=l1p.next
                prev.next=None
            else:
                if c==1:
                    res = l2p
                    prev = res
                    l2p=l2p.next
                    c+=1
                    print("[",res.val,"]")
                    continue
                prev.next = l2p
                prev =l2p
                l2p=l2p.next
                prev.next=None
            
            
            
            p = res
            
            print("[",end=" ")
            while p:
                print(p.val,end=", ")
                p=p.next
            print("]")
        if l1p:
            prev.next = l1p
        elif l2p:
            prev.next=l2p
            
        return res



                
        