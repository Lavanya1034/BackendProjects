# FIFO-queue


class MyQueue:
    def __init__(self):
        self.queue = list()

    def push(self, x: int):
        self.queue.append(x)

    def pop(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            return None

    def empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)


# creating an object for queue

queue1 = MyQueue()
queue1.push(1)
queue1.display()
queue1.push(2)
queue1.display()
queue1.pop()
queue1.display()
print(queue1.empty())
