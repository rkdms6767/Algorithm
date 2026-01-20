# Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 2이 존재한다면 True
# 존재하지 않는다면 False 를 반환하시오.
# [0, 3, 5, 6, 1, 2, 4]

finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

def is_existing_target_number_binary(target, array):
    # 구현해보세요!
    start_index = 0
    last_index = len(array) - 1
    middle_index = last_index // 2

    while start_index <= last_index:
        if target < array[middle_index]: #target이 더 작으면
            last_index = middle_index - 1
        elif target > array[middle_index]: #target이 더 크면
            start_index = middle_index + 1
        elif target == array[middle_index]: #target을 찾았으면
            return True
        middle_index = (start_index + last_index) // 2

    return False



result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)