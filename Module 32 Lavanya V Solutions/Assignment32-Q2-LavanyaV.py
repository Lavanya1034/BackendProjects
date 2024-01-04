# checking for balanced expression


class MyStack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)


def braces_check(braceInp):
    braceObj = {"(": ")", "[": "]", "{": "}"}
    arrBracesOpen = braceObj.keys()
    arrBracesClose = braceObj.values()
    # creating object with stack
    stackOb1 = MyStack()
    for i in range(len(braceInp)):  # updating stack with allowed braces
        if braceInp[i] in arrBracesClose or braceInp[i] in arrBracesOpen:
            stackOb1.push(braceInp[i])
    stackOb1.display()
    braceClose = []
    lenOfInpStack = len(stackOb1.stack)
    for x in range(lenOfInpStack):
        ele = stackOb1.pop()
        if ele in arrBracesClose:
            braceClose.append(ele)
        elif ele in arrBracesOpen:
            if len(braceClose) > 0:
                closeBraceOut = braceClose.pop()
                if not (braceObj[ele] == closeBraceOut):
                    return "The expression is not balanced"
            else:
                # this will handle when additional open braces is given
                return "The expression is not balanced"
    if len(braceClose) == 0:  # to handle extra closing braces in input
        return "The expression is balanced"
    else:
        return "The expression is not balanced"


t = int(input("Enter the no of test cases "))
for i in range(t):
    n = input("Enter the input  ")
    print(braces_check(n))
