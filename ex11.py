# Stack data structure implementation and max in a stack
class MaxStack(object):
    def __init__(self):
        self.stack = []
        self.maxes = []

    def push(self, val):         # append the value in the stack
        self.stack.append(val)
        if self.maxes and self.maxes[-1] > val:
            self.maxes.append(self.maxes[-1])
        else:
            self.maxes.append(val)

    def pop(self):          # pop the value in the stack
        if self.maxes:
            self.maxes.pop()
        return self.stack.pop()

    def max(self):
        return self.maxes[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())
print('max', s.max())
print(s.pop())


