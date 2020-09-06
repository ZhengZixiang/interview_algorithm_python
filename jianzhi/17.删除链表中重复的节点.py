# 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留。
#
# 样例1
# 输入：1->2->3->3->4->4->5
#
# 输出：1->2->5
# 样例2
# 输入：1->1->1->2->3
#
# 输出：2->3

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplication(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        while cur:
            while cur.next and cur.val == cur.next.val:
                cur = cur.next
            if pre.next == cur:
                pre, cur = cur, cur.next
            else:
                pre.next, cur = cur.next, cur.next
        return dummy.next
