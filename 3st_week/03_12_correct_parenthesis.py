def is_correct_parenthesis(string):
    # "(())()"  # True
    # "(((("  # False

    # (일 경우에는 스택에 넣기.
    # )인 경우에는 스택에서 pop해보기. 해봤는데 없으면, false break
    # 끝났는데 스택에 남아있으면 false
    # 그게 아니라 끝났는데 스택이 비어있으면 true.

    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        if char == ")":
            if not stack:
                return False
            pop_char = stack.pop()
    if stack:
        return False
    else:
        return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))