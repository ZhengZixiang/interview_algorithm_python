# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。 
# 
#  k 是一个正整数，它的值小于或等于链表的长度。 
# 
#  如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。 
# 
#  
# 
#  示例： 
# 
#  给你这个链表：1->2->3->4->5 
# 
#  当 k = 2 时，应当返回: 2->1->4->3->5 
# 
#  当 k = 3 时，应当返回: 3->2->1->4->5 
# 
#  
# 
#  说明： 
# 
#  
#  你的算法只能使用常数的额外空间。 
#  你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。 
#  
#  Related Topics 链表 
#  👍 711 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while pre:
            i = 0
            q = pre
            while i < k and q:
                q = q.next
                i += 1
            if not q:
                break
            a, b = pre.next, pre.next.next
            for i in range(0, k - 1):
                c, b.next = b.next, a
                a, b = b, c
            c = pre.next
            pre.next, c.next = a, b
            pre = c
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
