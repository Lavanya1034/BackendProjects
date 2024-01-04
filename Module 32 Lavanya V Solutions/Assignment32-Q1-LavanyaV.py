# string reverse using stack


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


def string_reverse(inp):
    # creating an object to reverse a stack

    stringInp = MyStack()

    # pushing string character wise
    for each in range(len(inp)):
        stringInp.push(inp[each])
    stringInp.display()
    arrOut = []
    for x in range(len(stringInp.stack)):
        if not (stringInp.isEmpty()):
            val = stringInp.pop()
            arrOut.append(val)
    return "".join(arrOut)


t = int(input("Enter the no of inputs  "))
for i in range(t):
    n = input("Enter the input string  ")
    print(string_reverse(n))
