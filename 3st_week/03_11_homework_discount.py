from collections import deque

def get_max_discounted_price(prices, coupons):
    merge_prices = merge_sort(prices)
    merge_coupons = merge_sort(coupons)
    queue_prices = deque(merge_prices)
    queue_coupons = deque(merge_coupons)

    # 1) merge_prices랑 merge_coupons을 popleft해서 빼면서.. 할인율 적용 후에 둘 중에 하나가 없어지면 종료.
    total_price = 0
    while True:
        if queue_prices and queue_coupons:
            current_price = queue_prices.popleft()
            current_coupon = queue_coupons.popleft()
            total_price += current_price * ((100 - current_coupon) / 100)
        elif queue_prices:
            for price in queue_prices:
                total_price += price
            break
        else:
            break
    return int(total_price)

# 제미나이가 알려준 더 나은 코드. while True 대신 조건 넣기.
# 1) 상품과 쿠폰이 둘 다 있을 때까지 깎아준다!
    while queue_prices and queue_coupons:
        current_price = queue_prices.popleft()
        current_coupon = queue_coupons.popleft()
        sum += current_price * ((100 - current_coupon) / 100)

    # 2) 그러고도 상품이 남았다면? (쿠폰이 부족한 상황)
    while queue_prices:
        sum += queue_prices.popleft()


def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    return merge(merge_sort(left_array), merge_sort(right_array))


def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] > array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))