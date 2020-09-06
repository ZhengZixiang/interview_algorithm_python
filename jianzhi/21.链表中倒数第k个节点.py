# 输入一个链表，输出该链表中倒数第k个结点。
#
# 注意：
#
# k >= 0;
# 如果k大于链表长度，则返回 NULL;
# 样例
# 输入：链表：1->2->3->4->5 ，k=2
#
# 输出：4

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def findKthToTail(self, pListHead, k):
        """
        :type pListHead: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not pListHead and k < 0:
            return None

        fast, slow = pListHead, pListHead
        for i in range(k):
            if fast:
                fast = fast.next
            else:
                return None

        while fast:
            fast = fast.next
            slow = slow.next
        return slow
