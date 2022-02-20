"""0또는 양의 정수가 주어졌을 때, 정수를 이러 붙여
만들 수 있는 가장 큰 수를 알아내주세요

예를 들어, 주어진 정수가 [6,10,2]라면
[6102,6210,1062,1026,2610,2106]을 만들 수 있고
이 중 가장 큰 수는 6210입니다.
0또는 양의 정수가 담긴 배열 numbers가 매개변수로
주어질 때, 순서를 재 배치하여 만들 수 있는 가장 큰 수를
문자열로 바꾸어 return하도록 solution함수를 작성해주세요

제한사항 
numbers의 길이는 1이상 100,000이하입니다.
numbers의 원소는 0이상 1,000이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 
return합니다."""
import math
def solution(numbers):
    # [6,10,2]
    #앞 자리가 가장 큰 수 찾기
    answer=""
    max=0
    print(sorted(numbers))
    for i in range(1,len(numbers)+1):
        for number in sorted(numbers):
            if len(str(number)) == 1:
                mok = number                 
            elif len(str(number)) != 1:                
                mok = number / int(math.pow(10,len(str(number))-1))
            if mok > max:
               max = mok
               z = number        
        answer += str(z)
        numbers.remove(z)
        max=0
    
    
    return print(answer)

numbers=[3, 30, 34, 5, 9]
solution(numbers)