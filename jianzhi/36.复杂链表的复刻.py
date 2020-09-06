# 请实现一个函数可以复制一个复杂链表。
#
# 在复杂链表中，每个结点除了有一个指针指向下一个结点外，还有一个额外的指针指向链表中的任意结点或者null。
#
# 注意：
#
# 函数结束后原链表要与输入时保持一致。

# Definition for singly-linked list with a random pointer.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#         self.random = None
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        orig = head
        while orig:
            copy = ListNode(orig.val)
            copy.next = orig.next
            orig.next = copy
            orig = copy.next

        orig = head
        while orig:
            if orig.random:
                orig.next.random = orig.random.next
            orig = orig.next.next

        orig = head
        copy = orig.next
        dummy = ListNode(-1)
        dummy.next = copy
        while orig:
            orig.next = orig.next.next
            if orig.next:
                copy.next = copy.next.next
            orig = orig.next
            copy = copy.next

        return dummy.next
