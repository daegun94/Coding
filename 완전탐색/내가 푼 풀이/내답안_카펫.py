"""Leo는 카펫을 사러 갔다가 아래 그림과 같이
중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로
칠해져 있는 격자 모양 카펫을 봤습니다.
Leo는 집으로 돌아와서 아까 본 카펫의
노란색과 갈색으로 색칠된 격자의 개수는
기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.
Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수
yellow가 매개변수로 주어질 때 카펫의 가로,
세로 크기를 순서대로 배열에 담아 return하도록 solution함수를 작성해주세요."""

"""갈색 격자의 수 brown은 8이상 5,000이하인 자연수
노란색 격자의 수 yellow는 1 이상 2,000,000이하인 자연수
카펫의 가로 길이는 세로 길이와 같거나 세로길이보다 김"""

"""전체 격자모양 수 -> row * col col은 무조건 3부터 시작(yellow가 1인경우 col = 3)
col을 기준으로 row 탐색
가로의 길이는 세로 길이와 같거나 길다" -> row >= col
yellow -> 1  row=3 col=3 
yellow -> 2  row=4 col=3 or row=3 col= 4 ->조건 충족 x
yellow -> 4  row=4 col =4  -> row * col == yellow가 되는 식 찾기."""

def solution(brown,yellow):
    total = brown+yellow
    answer=[]
    for col in range(3,total):
        row = int (total/col)
        if (row * col == total) & (row >= col) & ((row-2) * (col-2) == yellow): 
            answer=[row,col]
            break;
    
    return answer