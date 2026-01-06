#다음과 같이 영어로 되어 있는 문자열이 있을 때,
# 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약 그런 문자가 없다면 _ 를 반환하시오.
#"abadabac"

input = "abadabac"

def find_not_repeating_first_character(string):
    #빈도수 구하기
    #내가 알 수 있는 것: string의 char을 통해 해당하는 find_alphabet_occurrence_array에 접근할 수 있음.
    #                 , string에서 for문을 돌리면 빈도수 1을 찾았을 때 바로 return해줄 수 있음.
    find_alpha_occur = find_alphabet_occurrence_array(string) #[1,1,0,6,1,5]
    for char in string:
        char = char.lower()
        if not char.isalpha():
            continue
        num_to_occur = find_alpha_occur[ord(char) - ord('a')]
        if num_to_occur == 1:
            return char
    return "_"

    #첫번째 시도 - find_alpha_occur에서 for문을 돌려서 중첩for문 발생
    # not_repeat_list = []
    # find_alpha_occur = find_alphabet_occurrence_array(string)
    # smaller_index = len(string)  # 제일 작은 인덱스 담는 변수
    # for i, num in enumerate(find_alpha_occur): #num 1
    #     if num == 1: # i 3
    #         not_repeat_char = chr(i + 97) #b
    #         for j, char in enumerate(string):
    #             if not_repeat_char == char: #char b
    #                 if j < smaller_index: #더 작은 인데스를 찾아가는 과정
    #                     smaller_index = j
    #
    # if smaller_index == len(string):
    #     return "_"

    return string[smaller_index]


def find_alphabet_occurrence_array(string):
    alphabet_occurrence = [0] * 26 #빈도수를 담을 배열

    for char in string:
        char = char.lower()
        #파이썬의 == / !=: 내용물이 같은지 확인한다. (자바의 .equals() 역할)
        # 파이썬의 is / is not: 메모리 주소가 같은지 확인한다. (자바의 == 역할)
        if not char.isalpha():
            continue
        alphabet_occurrence[ord(char) - ord('a')] += 1

    print(alphabet_occurrence)

    return alphabet_occurrence


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("Abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))


#강사님의 정답
#
# def find_not_repeating_first_character(string):
#     alphabet_occurrence_array = [0] * 26
#
#     for char in string:
#         if not char.isalpha():
#             continue
#         arr_index = ord(char) - ord("a")
#         alphabet_occurrence_array[arr_index] += 1
#
#     not_repeating_character_array = []
#     for index in range(len(alphabet_occurrence_array)):
#         alphabet_occurrence = alphabet_occurrence_array[index]
#
#         if alphabet_occurrence == 1:
#             not_repeating_character_array.append(chr(index + ord("a")))
#
#     for char in string:
#         if char in not_repeating_character_array:
#             return char
#
#     return "_"
#
#
# result = find_not_repeating_first_character
# print("정답 = d 현재 풀이 값 =", result("abadabac"))
# print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
# print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))