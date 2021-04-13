# -*- coding:utf-8 -*-


class CircularQueue:
    def __init__(self, MAXSIZE=12):
        self.front = 0
        self.rear = 0
        self.maxsize = MAXSIZE
        self.queue = [None] * self.maxsize

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.maxsize == self.front

    def push(self, ele):
        if self.is_filled():
            raise IndexError("queue fall, cannot push. {};{}".format(self.front, self.rear))
        else:
            self.rear = (self.rear + 1) % self.maxsize
            self.queue[self.rear] = ele

    def pop(self):
        if self.is_empty():
            raise IndexError("queue empty, cannot pop. {};{}".format(self.front, self.rear))
        else:
            self.front = (self.front + 1) % self.maxsize
            return self.queue[self.front]

    def show(self):
        # if self.front < self.rear:
        #     return self.queue[self.front + 1:self.rear]
        # else:
        #     return self.queue[:self.rear] + self.queue[self.front:]
        return self.queue, self.front, self.rear


if __name__ == '__main__':
    queue = CircularQueue()
    for i in range(11):
        queue.push(i)
    print(queue.show())
    # print(queue.push(10))
    queue.pop()
    queue.pop()
    print(queue.show())
    queue.push(14)
    print(queue.show())
    queue.push(15)
    print(queue.show())
    queue.pop()
    print(queue.show())
    queue.push(16)
    print(queue.show())