# Q.  링크드 리스트에서 index번째 원소를 제거하시오.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        node = self.get_node(index - 1)
        next_node = node.next
        node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get_node(index - 1)
        # #prev_node구하는 과정 기본ver
        # count_index = 0
        # prev_node = self.head
        # while count_index < index - 1 :
        #     cur = prev_node.next
        #     count_index += 1
        next_node = self.get_node(index).next #get_node()이용해두 됨.
        prev_node.next = next_node

    # [0] [1]    [2]    [3]
    #     cur  index   index.next저장


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.delete_node(1) #3 12
linked_list.delete_node(0) #12
linked_list.print_all()