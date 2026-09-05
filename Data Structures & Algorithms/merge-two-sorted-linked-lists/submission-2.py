# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                # currentの矢印をlist1に向ける
                current.next = list1
                # currentをlist1に移動する
                current = current.next
                # 次のlist1に移動する
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy.next


## .nextもcurrent, list1などはどちらもnodeを指し示している
## listの最後になるとnoneに進むからその時点でloopが終わる