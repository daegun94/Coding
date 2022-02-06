
def solution(array, commands):
    answer = []
    for command in commands:
        #한번에 입력가능 j,j,k= 2,5,3
        i,j,k = command
        answer.append(list(sorted(array[i-1:j]))[k-1])
    return answer
array = [1,5,2,6,3,7,4]
commands = [[2,5,1]]
solution(array, commands)