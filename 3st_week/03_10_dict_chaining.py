class LinkedTuple:
    def __init__(self):
        self.items = []

    def add(self, key, value):
        self.items.append((key, value))

    #     items.append([key, value]): "이 데이터는 나중에 수정될 수도 있어."
    # items.append((key, value)): "이건 딱 고정된 한 쌍의 데이터야."

    def get(self, key):
        for k, v in self.items:
            if k == key:
                return v

class LinkedDict:
    def __init__(self):
        self.items = [LinkedTuple() for _ in range(8)]
    #     self.items = []
    #         for i in range(8):
    #             self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        self.items[index].add(key,value)

        # [ , , , , ,]
        # [["kk", 33],[],[] ]
        # [ ]

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)


my_dict = LinkedDict()
my_dict.put("test", 3)
print(my_dict.get("test"))  # 3이 반환되어야 합니다!