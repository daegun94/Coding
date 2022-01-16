def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        #idx 0, 1
        #  1 == pattern1[0%5] 답 = 패턴의 답 맞춘갯수 구함.
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1
    # 0,score[0] 1,score[1], 2,score[2]
    for idx, s in enumerate(score):
        # 수포자들의 점수가 max라면
        # 게다가 for문을 통해 중복 max도 검사할 수 있음.
        if s == max(score):
            result.append(idx+1)

    return result
answers=[1,2,3,4,5]
print(solution(answers))