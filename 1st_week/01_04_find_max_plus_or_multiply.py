#50->00
def find_max_plus_or_multiply(array):
    #0과 1을 만나면 + ? 아니면 +과 *를 각각 해본 다음 더 큰 수로 ?
#[1,0,3,5] -> max_num 에 순회하면서 0,1인 경우엔 +, 아닌경우엔 x
#1+0=1 1+3=4 4*5=20
#1 1 4(max_num이 0또는 1) 20
# [3,5,1]  3
# max_num = 0 -> 3 -> 15 -> 16
    if not array: return 0

    multiply_sum = array[0]
    for number in array[1:]:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number
    return multiply_sum

# for i in range(len(array)):
#         if i == len(array) - 1:
#             return array[i]
#
#         if array[i] + array[i + 1] > array[i] * array[i + 1]:
#            array[i + 1] = array[i] + array[i + 1]
#         else:
#             array[i + 1] = array[i] * array[i + 1]

#array를 바꾸지 않고 max를 찾아낸다면?
    # [0, 3, 5, 1]
    #i=0 a[0]과 a[0+1]계산 -> 결과값을 max 변수에
    #i=1 max와 a[1+1] 계산 ,,, i=2 일때 a[3] 계산 후 return
    # max_num = array[0]
    # for i in range(len(array)):
    #     if max_num + array[i + 1] > max_num * array[i + 1]:
    #        max_num += array[i + 1]
    #     else:
    #         max_num *= array[i + 1]
    #
    #     if i == len(array) - 2:
    #         return max_num

# i=0 / 0 + 3 -> [0,3,5]
# i=1/ 3 * 5 -> [0,3,15]
# i=2/ 15 * 없음. array[i]돌려주기


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))