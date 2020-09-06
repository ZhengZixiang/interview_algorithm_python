# 给定一个链表，若其中包含环，则输出环的入口节点。
#
# 若其中不包含环，则输出null。
#
# 样例
# QQ截图20181202023846.png
#
# 给定如上所示的链表：
# [1, 2, 3, 4, 5, 6]
# 2
# 注意，这里的2表示编号是2的节点，节点编号从0开始。所以编号是2的节点就是val等于3的节点。
#
# 则输出环的入口节点3.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def entryNodeOfLoop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        if fast == slow:
            slow = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow
        else:
            return None
