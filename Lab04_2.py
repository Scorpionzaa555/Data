class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        print(len(self.data))

    def is_empty(self):
        if self.data == []:
            return True
        else:
            return False

    def push(self, input_data):
        self.data.append(input_data)

    def pop(self):
        if self.data == []:
            return None
        else:
            value = self.data.pop(-1)
            return value

    def stackTop(self):
        if self.data == []:
            return None
        else:
            value = self.data[-1]
            return value

    def printStack(self):
        print(self.data)

def copyStack(stack1, stack2):
    if not stack2.is_empty():
        stack2.pop()

    

s1 = ArrayStack()
s1.push(10)
s1.push(20)
s1.push(30)
s2 = ArrayStack()
s2.push(15)
copyStack(s1, s2)
s1.printStack()
s2.printStack()
        