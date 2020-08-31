# 请用栈实现一个队列，支持如下四种操作：
#
# push(x) – 将元素x插到队尾；
# pop() – 将队首的元素弹出，并返回该元素；
# peek() – 返回队首元素；
# empty() – 返回队列是否为空；
# 注意：
#
# 你只能使用栈的标准操作：push to top，peek/pop from top, size 和 is empty；
# 如果你选择的编程语言没有栈的标准库，你可以使用list或者deque等模拟栈的操作；
# 输入数据保证合法，例如，在队列为空时，不会进行pop或者peek等操作；
# 样例
# MyQueue queue = new MyQueue();
#
# queue.push(1);
# queue.push(2);
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop(-1))
        return self.s2.pop(-1)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop(-1))
        return self.s2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.s1 and not self.s2:
            return True
        return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
