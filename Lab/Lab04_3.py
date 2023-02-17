class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

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

def infixToPostfix(expression):
    stack1 = ArrayStack()
    operator = {"+":1, "-":1, "*":2, "/":2}
    blank = ""
    for i in expression:
        if i.isalpha():
            blank += i
        else:
            if not stack1.is_empty():
                while not stack1.is_empty():
                    if operator[i] <= operator[stack1.stackTop()]:
                        blank += stack1.pop()
                        continue
                    break
            stack1.push(i)
    while not stack1.is_empty():
        blank += stack1.pop()
    return blank

exp = "A+B*C/D-E+F*G"
postfix = infixToPostfix(exp)
print("Postfix of", exp, "is", postfix)
