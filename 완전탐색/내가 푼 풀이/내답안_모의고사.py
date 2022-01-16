"""수포자는 수학을 포기한 사람의 준말입니다.
수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.
1번 수포자:1,2,3,4,5,1,2,3,4,5,...
2번 수포자:2,1,2,3,2,4,2,5,2,1,2,3,2,4,2,5,...
3번 수포자:3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5,...
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return하도록
solution 함수를 작성."""

#제한조건:
#시험문제는 최대 10,000문제로 구성되어있음.
#문제의 정답은 1,2,3,4,5,중 하나.
#가장 높은 점수를 받은 사람이 여럿일 경우,
#return하는 값을 오름차순으로 정렬

#ex) [1,2,3,4,5] -> return [1]
#[1,3,2,4,2] -> return [1,2,3]


#내 생각
#수포자들의 규칙을 찾고 
#정답 배열 answers와 비교하며 수포자들의 맞춘횟수 세기.

def solution():
    #정답이 들은 배열->answers
    #정답 기준 갯수 새기(answers)
    answers=[1,3,2,4,2]
    answers_n1,answers_n2,answers_n3=[],[],[]
    count = 0
    sum_n1,sum_n2,sum_n3 = 0,0,0
    #수포자의 정답 배열.
    #[1,2,3,4,5] [2,1,2,2,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]
    #answers가 홀 수 일때
    #[1,2,3,4,5,1,2,3,4] , [2,1,2,2,2,3,2,4,2], [3,3,1,1,2,2,4,4,5]

    #1번 수포자 정답 배열 구하기 ->answers_n1
    for i in range(1,len(answers)+1):
        count+=1
        if count < 6:
            answers_n1.append(count)
        elif count > 5:
            count = 1
            answers_n1.append(count)

    count = 0
    #2번 수포자 정답 배열 구하기 -> answers_n2        
    for i in range(2,len(answers)+2):
        if i % 2 == 0:  
            answers_n2.append(2)
        elif i % 2 ==1:
            count += 1
            if count < 6:
                answers_n2.append(count)
            else :
                count = 1
                answers_n2.append(count) 
    count = 0
    #3번 수포자 정답 배열 -> answers_n3
    for i in range(1,len(answers)+1):
        if count == 0 or count == 1:
            answers_n3.append(3)
        if count == 2 or count == 3:
            answers_n3.append(1)
        if count == 4 or count == 5:
            answers_n3.append(2)
        if count == 6 or count == 7:
            answers_n3.append(4)
        if count == 8 or count == 9:
            answers_n3.append(5)
        if count > 9:
            count = 0
        count += 1
    for i in range(0,len(answers)):
        if (answers_n1[i] == answers[i]):
            sum_n1 += 1
        if (answers_n2[i] == answers[i]):
            sum_n2 += 1
        if (answers_n3[i] == answers[i]):
            sum_n3 += 1
    if sum_n1 - sum_n2 > 0 and sum_n2 - sum_n3 >= 0:
        return [1]
    if sum_n1 - sum_n2 > 0 and sum_n1 - sum_n3 <=0: 
        return [3]
    if sum_n1 - sum_n2 < 0 and sum_n2 - sum_n3 >=0:
        return [2]
    if sum_n1 == sum_n2 and sum_n1 - sum_n3> 0:
        return [1,2]
    if sum_n1 == sum_n2 == sum_n3:
        return [1,2,3]
    if sum_n2 == sum_n3 and sum_n2 - sum_n1 >0:
        return [2,3]



solution()
      
