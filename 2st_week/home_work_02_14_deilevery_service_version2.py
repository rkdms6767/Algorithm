# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.


shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus_set = set(menus) # O(N) set: 해시 충돌을 방지하기 위해 실제 데이터보다 훨씬 큰 메모리 공간을 미리 할당해 둬야 합니다.
    for order in orders:
        if order not in menus_set:         #O(1) !?!?    <--- O(logN)
            return False
    return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)