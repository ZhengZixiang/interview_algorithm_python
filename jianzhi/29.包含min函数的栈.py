# 设计一个支持push，pop，top等操作并且可以在O(1)时间内检索出最小元素的堆栈。
#
# push(x)–将元素x插入栈中
# pop()–移除栈顶元素
# top()–得到栈顶元素
# getMin()–得到栈中最小元素
# 样例
# MinStack minStack = new MinStack();
# minStack.push(-1);
# minStack.push(3);
# minStack.push(-4);
# minStack.getMin();   --> Returns -4.
# minStack.pop();
# minStack.top();      --> Returns 3.
# minStack.getMin();   --> Returns -1.

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.min_stack and self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop(-1)
        self.stack.pop(-1)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
