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
            print(value)

    def printStack(self):
        print(self.data)

myStack = ArrayStack()
myStack.push(10)
myStack.push(20)
myStack.push(30)
#myStack.stackTop()
myStack.printStack()
x = myStack.pop()
print(x)
myStack.pop()
myStack.printStack()
myStack.pop()
print(myStack.is_empty())
myStack.pop()