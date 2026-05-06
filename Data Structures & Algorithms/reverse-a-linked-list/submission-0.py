# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current_node = head
        next_node = current_node.next if current_node.next else None
        current_node.next = None  # missed this


        while next_node:

            # print("cn:",current_node.val,"nn:",next_node.val, end=" ")
            
            next_node_p = next_node.next

            # print("nnp:",next_node_p.val if next_node_p else "NA", end=" ")

            next_node.next = current_node
            current_node = next_node
            next_node = next_node_p

            # break

            # print("cn:",current_node.val,"nn:",next_node.val if next_node else "NA","nn.n",next_node.next.val if next_node and next_node.next else "NA")

        return current_node


            


        