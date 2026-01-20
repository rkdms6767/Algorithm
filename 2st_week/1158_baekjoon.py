import sys

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

    def readAll(self):
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

    def delete_node(self, index):
        if index == 0:
            self.head = self.head.next
            return
        prev_node = self.get_node(index - 1)
        next_node = self.get_node(index).next  # get_node()이용해두 됨.
        prev_node.next = next_node


def make_linked_list(size_of_list):
    linked_list = LinkedList(1)
    for i in range(2, size_of_list + 1):
        linked_list.append(i)
    return linked_list

def make_josephuse(linked_list, remove_num):
    josephuse_list = []
    count = 1
    linked_list_cur = linked_list.head
    linked_list_index = 0

    while linked_list.head is not None:

        if linked_list_cur is None:
            linked_list_cur = linked_list.head
            linked_list_index = 0
            # count += 1
        else:
            linked_list_cur = linked_list_cur.next
            linked_list_index += 1
            count += 1

        if count == remove_num:

            if linked_list_cur is None: #4 -> x
                josephuse_list.append(linked_list.head.data)
                linked_list.delete_node(0)
            else:
                josephuse_list.append(linked_list_cur.data)

                linked_list.delete_node(linked_list_index)

                linked_list_cur = linked_list_cur.next
                count = 1
            # linked_list_index += 1
            continue


    return josephuse_list


input_data = sys.stdin.read().split()
if input_data:
    N = int(input_data[0])
    K = int(input_data[1])

    linked_list1 = make_linked_list(N)

    result = make_josephuse(linked_list1, K)
    print("<" + ", ".join(map(str, result)) + ">")





