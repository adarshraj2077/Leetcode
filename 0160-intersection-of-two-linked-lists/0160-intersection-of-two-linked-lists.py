# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        i = headA
        temp = headA
        j = headB
        new = headB
        countA = 0
        countB = 0

        while temp is not None:
            temp = temp.next
            countA += 1
        # print(countA)

        while new is not None:
            new = new.next
            countB += 1
        # print(countB)


        if countA>countB:
            diff = countA - countB

            while diff > 0:
                i = i.next
                diff -= 1

        else:
            diff = countB - countA

            while diff > 0:
                j = j.next
                diff -= 1

        
        while i != j:
            i = i.next
            j = j.next

        return i