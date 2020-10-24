class Stack:

    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        removed = self.stack[self.size - 1]
        self.stack = self.stack[:self.size - 1]
        self.size -=1
        
        return removed

    def peek(self):
        return self.stack

    def isEmpty(self):
        return self.size == 0

    def size(self):
        return self.size


# s = Stack()

# print(s.isEmpty())
# s.push(4)
# s.push("dog")
# s.push(True)
# print(s.size)
# print(s.isEmpty())
# s.push(8.4)
# print(s.pop())
# print(s.pop())
# print(s.stack)
# print(s.size)

def revstring(myStr):
    stack = Stack()

    for i in range(len(myStr)):
        stack.push(myStr[len(myStr) - 1 - i])
    
    return "".join(stack.peek())


# print(revstring("hello"))

