from collections import defaultdict

def get_melon_best_album(genre_array, play_array):
    # 1)반복문
    # genres와 play_array를 같이 돌면서
    # 완료 후, 장르list와 플레이리스트list 값 배치 완료.

    genre_total_play_dict = {} #{"classic":240, "pop":550}
    genre_index_play_array_dict = {} #{"classic":[[0,10],[2,50],   ] , "pop":550}
    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        if genre_array[i] not in genre_total_play_dict:
            genre_total_play_dict[genre] = play
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play
            genre_index_play_array_dict[genre].append([i, play]) #[[i, play]]로 써서 오류났었음..

    # print("genre_total_play_dict.items()", genre_total_play_dict.items())
    # 결과:                   dict_items([('classic', 1450), ('pop', 3100)])
    genre_total_play_dict = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True) #정렬된 딕셔너리객체 꼭 담으시오!~!~!~

    result = []
    for genre, value in genre_total_play_dict: #딕셔너리에서 꺼낼때는 인자 두개 놓기!!
        index_play_array = genre_index_play_array_dict[genre] #[[0,10],[2,50],   ]

        # print("index_play_array", index_play_array)
        # 결과:                [[1, 600], [[4, 2500]]

        sorted_index_play_array = sorted(index_play_array,key = lambda array: array[1], reverse = True)

        # #sorted_index_play_array가 2개 이하인경우도 생각해야함..

        # for i in range(2):
        #     if sorted_index_play_array[i] is None:
        #         break
        #     else:
        #         result.append(sorted_index_play_array[i][0])
        # 현재 testcase는 잘 나오지만,
        # 이렇게 하면 None이 들었는지 확인하기도 전에 indexError난대.....

        # # 방법 1: 길이로 확인하기 (전통적인 방식)
        # for i in range(2):
        #     if i < len(sorted_index_play_array):  # i가 방 개수보다 작을 때만!
        #         result.append(sorted_index_play_array[i][0])
        #     else:
        #         break  # 방이 없으면 탈락!

        # 방법 2: 슬라이싱 (파이썬 고수 방식)
        for song in sorted_index_play_array[:2]:  # 알아서 있는 만큼만(최대 2개) 가져옴!
            result.append(song[0])

    return result


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))


# ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
# 장르list = 오로지 합계만 구하는.
# 플레이리스트list = 각 geners을 key로 하는 play(인덱스,값) 저장
#
# 1)반복문
# genres와 play_array를 같이 돌면서
# 완료 후, 장르list와 플레이리스트list 값 배치 완료.
#
#2)합계 내림차순으로 정렬.
#3)정렬된 genres기준으로 플list에 접근.
#플list 내림차순 정렬. (같은 값 있을시?) 후 앞에 두개만 새로운list에 추가.

# {'classic': 1450, 'pop': 3100}
# {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]}







# ["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]
# 튜플list = (value, index)로 이루어져 있는 list
# 딕셔너리list = 튜플list로 이루어진 배열. 인덱스는 key의 hash값.
# genres와 play_array를 같이 돌면서, generes를 딕셔너리list에 key로, play_array를 꺼내서
# 각 generes에 대한 합계를 구해주면서. 각 key에 대한 인덱스리스트에 value와 index를 넣어준다.
#
# classic의hash값으로 인덱스            pop의hash값으로인덱스
# [[합계,튜플list],                        [합계,튜플list]]
#     ↓                                          ↓
#   [[500,0],[150,2],[800,3]]           [[600,1],[2500,4]]
#
# 딕셔너리list를 큰 순위대로 정렬.
# 두개씩 뽑아 result_list에 넣기...

############stop - 너무 복잡하게 접근함.
