# Q. 배달의 민족 서버 개발자로 입사했다.
# 상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
#
# 그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
#
# menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
# orders = ["오뎅", "콜라", "만두"]

# menus 돌때 orders에 있는지 하나하나 체크 후 orders 삭제 2^N
# xxx orders 돌 때 menus에 있는지 하나하나 체크.. 너무 오래 걸리는데 다른 방법이 없으니!
# 도는 걸 줄여주는 이분법으로 접근하자.

# 없는 값을 넣었을 때 프로그램이 안 끝난다면 while 조건이나 break가 빠진 거.
shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders): #(NlogN) + O(M) * O(logN) = O((M+N)log(N))
    menus.sort()  # O(NlogN) -> 정렬된 데이터가 들어온 경우 필요 없음.
    for order in orders: #O(M)
        if not is_existing_target_number_binary(order, menus): #(logN)
            return False
    return True

#version2의 set과 다르게 이분 탐색을 할 때의 장점은?
# 이분 탐색: "콜라는 없는데, 가장 비슷한 이름인 '사이다'는 있어!" 또는 "예산 5,000원으로 살 수 있는 가장 비싼 메뉴가 뭐야?" 같은 질문에 답할 수 있습니다.
#
# 즉, 범위 탐색이나 근삿값 찾기가 필요할 때는 무조건 이분 탐색입니다.

def is_existing_target_number_binary(target, array):
    current_min = 0
    current_max = len(array) - 1
    current_guess = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_guess] == target:
            return True
        elif array[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        current_guess = (current_min + current_max) // 2

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)