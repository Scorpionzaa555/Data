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
            print("5555555")
            return None
        else:
            value = self.data.pop(-1)
            return value

    def printStack(self):
        print(self.data)

def is_parentheses_matching(expression):
    st3 = ArrayStack()
    for i in expression:
        if i == "(":
            st3.push(i)
        elif i == ")":
            if not st3.is_empty():
                st3.pop()
            else:
                print("Parentheses in", expression, "are unmatched")
                return False

    if st3.is_empty():
        return st3.is_empty()
    else:
        print("Parentheses in", expression, "are unmatched")
        return st3.is_empty()

pharsing = ArrayStack()
str = ")((((((((((((A-B)*C)))))"
result = is_parentheses_matching(str)
print(result)

pharsing = ArrayStack()
str = "(((A-B)*C)"
result = is_parentheses_matching(str)
print(result)
