# 0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다. 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
#
# 예를 들어 S=0001100 일 때,
#
# 전체를 뒤집으면 1110011이 된다.
# 4번째 문자부터 5번째 문자까지 뒤집으면 1111111이 되어서 2번 만에 모두 같은 숫자로 만들 수 있다.
# 하지만, 처음부터 4번째 문자부터 5번째 문자까지 문자를 뒤집으면 한 번에 0000000이 되어서 1번 만에 모두 같은 숫자로 만들 수 있다.
#
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.


# 00000 11111 0001100 111101 010011100011
# 숫자가 바뀌는 지점 0->1 1->0 에서 count++ / flag로 0인지 1인지
# 뒤집어야할 조건은 바뀌는 지점 + 이 전 문자와 같으면 패스
input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    if not string.isdigit():
        return "-1"
    flag = string[0] #0
    before_num = string[0]
    turn_out_count = 0
    for num in string: # 1
        if num != flag and before_num != num:
            turn_out_count+=1
        before_num = num
    return turn_out_count


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# '1'이 덩어리 1개 ("111")
# '0'이 덩어리 2개 ("0", "00")
# 정답은? 1 (111을 뒤집어서 000000으로 만드는 게 더 빠름!)
# 가은님 코드 결과는? (아마 1이 나올 것 같아요. '0'이 flag가 되니까요!)
print("결과:", find_count_to_turn_out_to_all_zero_or_all_one("011100"))

# 자, 그럼 이건 어떨까요? (이게 진짜입니다!)
# '0' 덩어리: 1개 ("000")
# '1' 덩어리: 2개 ("1", "1") -> 첫 번째 숫자가 1임!
# 정답은? 1 (가운데 000을 뒤집는 게 빠름)
# 가은님 코드 결과는?
print("결과:", find_count_to_turn_out_to_all_zero_or_all_one("10001"))