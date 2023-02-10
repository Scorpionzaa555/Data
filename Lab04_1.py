class ArrayStack:
    def __init__(self):
        self.data = []

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

    def printStack(self):
        print(self.data)

    def is_parentheses_matching(self, expression):
        for i in expression:
            if i == "(":
                self.push(i)
            elif i == ")":
                self.pop()

        if self.data != []:
            print("Parentheses in", expression, "are unmatched")
        return self.is_empty()

pharsing = ArrayStack()
str = "(((A-B)*C)"
result = pharsing.is_parentheses_matching(str)
print(result)
