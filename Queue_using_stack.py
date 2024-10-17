#https://leetcode.com/problems/implement-queue-using-stacks/?envType=problem-list-v2&envId=queue
#code:
class MyQueue(object):

    def __init__(self):
        self.stack=deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #n=len(self.stack)
        self.stack.append(x)

        

    def pop(self):

        """
        :rtype: int
        """
        return self.stack.popleft()
        

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]
      
        

    def empty(self):
        """
        :rtype: bool
        """
        return not  self.stack
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()