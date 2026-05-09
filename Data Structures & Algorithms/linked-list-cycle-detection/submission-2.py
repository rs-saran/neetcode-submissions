class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        else:
            sp = head
            fp = head

            while fp and fp.next:
                sp = sp.next
                fp = fp.next.next
                
                if sp == fp:
                    return True
            
            return False



        