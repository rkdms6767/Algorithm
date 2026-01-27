# Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
# [6] -> [7] -> [8] # 이런 링크드 리스트가 입력되었을 때,
#                   # 끝에서 2번째 값은 7을 반환해야 합니다!

# 두개의 포인터 사용
# 끝에 도달했을 때 k번째 앞인 포인터를 이용해 바로 반환!

#O(n) 으로 시간복잡도가 크게 변화되지는 않음.

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

    def get_kth_node_from_last(self, k):
        slow = self.head
        #k만큼 떨어진 포인터
        fast = slow
        for i in range(k):
            fast = fast.next

        while fast is not None:
            fast = fast.next
            slow = slow.next

        return slow


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!