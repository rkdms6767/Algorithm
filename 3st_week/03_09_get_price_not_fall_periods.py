prices = [1, 2, 3, 2, 3]


def get_price_not_fall_periods(prices):
    answer = []
    for start_index in range(len(prices)): #0-4
        count = 0
        for index in range(start_index+1, len(prices)): #start_index+1-4
            count += 1
            if prices[start_index] > prices[index]:
                break
        answer.append(count)
    return answer

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))