class MyStack:
    def __init__(self):
        self.stackArray = list()
    def push(self, data):
        self.stackArray.append(data)
    def pop(self):
        return self.stackArray.pop()
    def peek(self):
        return self.stackArray[-1]
    def size(self):
        return len(self.stackArray)
    def is_empty(self):
        if self.size() > 0:
            return False
        else:
            return True
