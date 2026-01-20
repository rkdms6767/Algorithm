# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
# [6] -> [7] -> [8] # 이런 링크드 리스트가 입력되었을 때,
#                   # 끝에서 2번째 값은 7을 반환해야 합니다!
# O(n)예상. 몇개인지 알아내고, 해당하는 곳까지 옮겨가서 데이터 보내기

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

#리스트 개수 세는 함수
    def count(self):
        count = 0
        cur = self.head
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def get_kth_node_from_last(self, k):
        total_count = self.count()
        count_num = 0
        cur = self.head                       # [1] [2] [3]
        while count_num < (total_count - k):   # 1 < 3 - 2 뒤에서 두번째
            count_num += 1
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!