# Finding the first pair of nos = given no
# can be implemented using queue


class MyQueue:
    def __init__(self):
        self.queue = list()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def isEmpty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)


def find_add_nos(no, tarrgetNo):
    # object created
    obj1 = MyQueue()
    # pushing elements to queue object
    for i in no:
        obj1.enqueue(i)
    while not (obj1.isEmpty()):
        noPoppedOut = obj1.dequeue()
        diff = target - noPoppedOut
        if diff in obj1.queue:
            return (noPoppedOut, diff)

    return "No Pairs Found"


n = [int(x) for x in input("Enter the elements   ").split()]
target = int(input("Enter the target no  "))
print(find_add_nos(n, target))
