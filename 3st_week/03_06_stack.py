class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
        return

    # pop 기능 구현
    def pop(self):
        if self.is_empty():
            return "Stack is empty!"
        delete_head = self.head
        self.head = delete_head.next
        return delete_head.data

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"

        return self.head.data

    # isEmpty 기능 구현
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(4)
stack.push(2)
print(stack.peek())
print(stack.pop())
print(stack.pop())
print(stack.pop())