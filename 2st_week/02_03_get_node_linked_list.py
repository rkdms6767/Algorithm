# Q.  링크드 리스트에서 index번째 원소를 반환하시오. get_node
# Q.  링크드 리스트에서 index번째 원소를 추가하시오. add_node

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
        cur = self.head
        count_index = 0
        while count_index != index : #count 5 index5 #range(0,index)
            cur = cur.next
            count_index += 1
        return cur

    def add_node(self, index, value):
        new_node = Node(value)

        # 만약 맨 앞에 추가하는 경우(index 0)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return


        cur = self.head
        count_index = 0

        while count_index < index - 1: #count_index 3 index 5
            count_index += 1 #4
            cur = cur.next #4

        new_node.next = cur.next
        cur.next = new_node

    #index 0에 추가할때는
    # [1][5][13][4]
    #  /
    # [5] head


    #                 2      3
    # [5] -> [12] -> [6] -> [8]
    #
    #               !cur index
    #                 2    3    4
    # [5] -> [12] -> [6]   ->   [8]
    #                     [31]

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.add_node(2, 13)
linked_list.print_all()