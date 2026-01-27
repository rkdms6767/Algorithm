input = [4, 6, 2, 9, 1]
# 1단계
# [4, 6, 2, 9, 1]
#     1 들어와
# [4, 6]
#  0이랑 비교            0
#
# 2단계
# [4, 6, 2, 9, 1]
#        2 들어와
#     1이랑 비교         1 0
# 0이랑 비교
#
# 3단계
# [4, 6, 2, 9, 1]
#           3들어와      2 1 0
#        2
#     1
# 0
#
# 4단계
# [4, 6, 2, 9, 1]
#              4들어와   3 2 1 0
#           3
#        2
#     1
# 0이랑 비교


def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break

    return array

# 강사님 정답
# def insertion_sort(array):
#     n = len(array)
#     for i in range(1, n):
#         for j in range(i):
#             if array[i - j - 1] > array[i - j]:
#                 array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
#             else:
#                 break
#     return array

# 1일때 0
#   빼주면 1
# 2일때 0 1
#   빼주면 2 1

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))