def find_max_occurred_alphabet(string):
    alphabet_array = find_alphabet_occurrence_array(string) #알파벳 빈도수를 담은 배열
    max = 0 # 가장 큰 값을 저장
    max_char = '' #max일 경우 같이 업데이트 되는 알파벳
    #max일 경우의 index를 저장하는 max_index 변수를 만들어서 저장한다음, 마지막 return 때 숫자를 알파벳으로 변환시켜도 됨.
    for i in range(len(alphabet_array)): #0..25
        alphabet_frequency = alphabet_array[i] #3
        if max < alphabet_frequency: #최고 빈도수라면
            max = alphabet_frequency # 가장 큰 값 업데이트
            max_char = chr( i + ord('a')) # 빈도수 가장 큰 알파벳도 업데이트
            #max = 3 -> 해당하는 인덱스 i 가 어떤 알파벳인지 알아야함.
            # 0 - 26 이고, 0일 경우에는 0(i) + 97 을 다시 chr()로 변환.
    return max_char


def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    #문장을 돌면서, 해당하는 문자에 대한 배열인덱스값에 숫자를 증가시켜준다.
    for char in string:
        char.lower()
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array


print("정답 = [1, 0, 2, 2, 2, 0, 2, 1, 3, 0, 0, 2, 2, 3, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("hello my name is dingcodingco"))
print("정답 = [1, 0, 0, 0, 2, 0, 1, 1, 1, 0, 0, 2, 1, 0, 2, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("we love algorithm"))
print("정답 = [0, 3, 0, 0, 3, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 1, 0] \n현재 풀이 값 =",
      find_alphabet_occurrence_array("best of best youtube"))

result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))