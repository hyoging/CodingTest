def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        # Ture에 해당하는 요소(item)는 더한다.
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer


a = [4, 7, 12]
s = [True, False, True]
print(solution(a, s))


