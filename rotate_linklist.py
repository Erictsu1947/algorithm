# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        if k < 1:
            return head

        cur = head

        length = 1
        while cur.next is not None:
            length += 1
            cur = cur.next

        k %= length
        if k == 0:
            return head

        first = head
        temp = head
        while k > 0:
            k -= 1
            temp = temp.next
        while temp.next is not None:
            first = first.next
            temp = temp.next

        res = first.next
        first.next = None
        temp.next = head
        return res

item_1 = ListNode(1)
item_2 = ListNode(2)
item_1.next = item_2

res = Solution().rotateRight(item_1, 1)
while res is not None:
    print(res.val)
    res = res.next
