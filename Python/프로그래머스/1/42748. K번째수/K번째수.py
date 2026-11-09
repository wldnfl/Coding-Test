def solution(array, commands):
    answer = []
    for cmd in commands:
        i, j, k = cmd
        sliced = sorted(array[i-1:j])
        answer.append(sliced[k-1])
    return answer