from itertools import permutations
#permutation
#permutation("ABCD",2)->AB AC AD BA BC BD CA CB CD DA DB DC
#permutation(range(3))-->0123 021 102 120 201 210
def solution(n):
    #비어있는 set집합 생성
    #set특징 중복제거
    a = set()
    for i in range(len(n)):
        #map(적용시킬함수,적용할값들)
        #ex(+1함수,(리스트나튜플))
        #ex(+1함수,([1,2,3,4,5])) -> (2,3,4,5,6) *map객체로 반환되어
        #list로 감싸줘서 변환시켜야함.
        #permutaitions(list(n),i+1) -> 조합 수 반환
        #"".join -> join함수는 리스트를 문자열로 합쳐주는 함수 ex) ['a','b','c'] -> "abc" 
        # |= 왼쪽값과 오른쪽값을 합친 것
        # -= 왼쪽변수에 오른쪽 값을 뺀 값을 왼쪽에 저장.
        #0,1을제외시킴.
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    a -= set(range(0, 2))

    #약수는 대칭적으로 나오기때문에 약수 찾을땐 제곱근까지만 찾으면됨.
    for i in range(2, int(max(a) ** 0.5) + 1):
        #소수구하는 알고리즘중인 에라토스테네스의 체..
        #2는 첫 소수 2의 배수를 다 제외
        #그다음 소수는 3 3의배수를 다제외
        #그다음 소수는 5 5의 배수를 다 제외
        #그다음 소수는 7 7의배수를 다 제외
        #구간마다 제외되지 않은 수가 소수.
        a -= set(range(i * 2, max(a) + 1, i))
    return len(a)


