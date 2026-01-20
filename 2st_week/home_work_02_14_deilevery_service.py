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


def is_available_to_order(menus, orders):
    menus.sort()
    print("menus:", menus)
    for order in orders: #오뎅
        print("현재 order: ", order)
        return_flag = False
        start_index = 0
        end_index = len(menus) - 1
        middle_index = (start_index + end_index) // 2
        while start_index <= end_index:
            print("현재 start:", start_index, "현재 end:", end_index, "현재 middle:", middle_index)
            if menus[middle_index] == order:
                return_flag = True
                break
            elif menus[middle_index] < order:
                start_index = middle_index + 1
                middle_index = (start_index + end_index) // 2
            elif menus[middle_index] > order:
                end_index = middle_index - 1
                middle_index = (start_index + end_index) // 2
        if not return_flag:
            return False
    return True

result = is_available_to_order(shop_menus, shop_orders)
print(result)