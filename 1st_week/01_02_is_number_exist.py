def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    #array를 돌면서 number가 있으면 true로 바꾸어준다.
    for num in array: #N
        if num == number: # N * 1
            return True
    return False

#최선의 경우에는 1만큼의 연산, 최악의 경우에는 N만큼의 연산
#시간복잡도가 N이어도 최악, 최선이 달라질 수 있음.
#최악의 경우를 대비해서 알고리즘 성능 파악이 맞음.

result = is_number_exist
print("정답 = True 현재 풀이 값 =", result(3, [3,5,6,1,2,4]))
print("정답 = Flase 현재 풀이 값 =", result(7, [6,6,6]))
print("정답 = True 현재 풀이 값 =", result(2, [6,9,2,7,1888]))