# Q.  다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오.
#
# 예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
# 각각 678, 354 이므로 두개의 총합
# 678 + 354 = 1032 를 반환해야 한다.
#
# 단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.
#
# [6] -> [7] -> [8]
# [3] -> [5] -> [4]


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


def get_linked_list_sum(linked_list_1, linked_list_2):
    return get_number_of_linked_list(linked_list_1) + get_number_of_linked_list(linked_list_2)

# 0+6=6 6*10+7=67 67*10+8=678
def get_number_of_linked_list(linked_list):
    total_sum = 0
    current_node = linked_list.head
    while current_node is not None:
        total_sum = (total_sum * 10) + current_node.data
        print("current_node data: " , current_node.data)
        print("sum: " , total_sum)
        current_node = current_node.next
    print(total_sum)
    return total_sum

linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))