# 1에서 16까지 오름차순으로 정렬되어 있는 배열이 있다.
# 이 배열 내에 14가 존재한다면 True, 존재하지 않는다면 False 를 반환하시오.
finding_target = 5
finding_numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
                            # 3  4
                            # s  l
                            # m
def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    start_index, last_index = 0, len(array)
    middle_index = last_index // 2
    # while start_index != last_index:

    while start_index != last_index:
        if target < array[middle_index]: #target이 더 작으면
            last_index = middle_index - 1
            middle_index = (start_index + last_index) // 2
        elif target > array[middle_index]: #target이 더 크면
            start_index = middle_index + 1
            middle_index = (start_index + last_index) // 2
        elif target == array[middle_index]: #target을 찾았으면
            return True
    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)