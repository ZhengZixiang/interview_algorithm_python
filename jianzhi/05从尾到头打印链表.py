# 输入一个链表的头结点，按照 从尾到头 的顺序返回节点的值。
#
# 返回的结果用数组存储。
#
# 样例
# 输入：[2, 3, 5]
# 返回：[5, 3, 2]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def printListReversingly(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]
