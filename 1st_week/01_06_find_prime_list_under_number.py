import math
# Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오.
#
# 소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
# 나%나 = 나머지0 / 1~나-1 % 나 = 0이 나오면 소수  -> for문
# 20 1~20 그 안에서 또 for문
input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    list_of_prime = []
    for i in range(2, number + 1): # 2~20
        for j in range(2, int(math.sqrt(i)) + 1): # 2~10(i가20) 2 3 4 5 6 7 8 9 10
            if i % j == 0:
                break #소수아님
        else: #break를 만나지 않고 잘 내려왔다면
            list_of_prime.append(i)
    return list_of_prime

# 4는 소수 아님. 4%2=x 4%3=o
# 3은 소수. 3%2=o

for i in range(1,2):
    print("range=", i)


result = find_prime_list_under_number(input)
print(result)