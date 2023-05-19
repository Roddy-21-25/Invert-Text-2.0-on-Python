from collections import deque
stack = deque()

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
        print(self.container)

    def reverse_string(self, val):
        self.push(val)
        for str in self.container:
            print(str[::-1])

s = Stack()
s.reverse_string("91-DIVOC someratsiuqnoC")







