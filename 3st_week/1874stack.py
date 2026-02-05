# 1 2 3 4 5 6 7 8 9 10
#
# 1 2 3 4
#      pop -
#
# 1 2 3
#     pop -
#
# 1 2 5    want 3
#
#          want 2

import sys

def stack_sequence(n, sequence):
    count = 1
    stack = []
    s_index = 0
    result = []

    while s_index < n:
        if len(stack) == 0:
            stack.append(count)
            result.append("+")
            count += 1

        elif sequence[s_index] == stack[-1]:
            stack.pop()
            result.append("-")
            s_index += 1
            if s_index == n:
                break

        elif sequence[s_index] > stack[-1]:
            stack.append(count)
            result.append("+")
            count += 1

        elif sequence[s_index] < stack[-1]:
            print("NO")
            result = []
            break

    if len(stack) == 0:
        for char in result:
            print(char)

n = int(sys.stdin.readline())
sequence = [int(sys.stdin.readline()) for _ in range(n)]
stack_sequence(n, sequence)