from itertools import permutations
n = "234"

for i in range(len(n)):
    #[2,3,4] 0,1,2
    #permutations([2,3,4],1)
    #permutations([2,3,4],2)
    #permutations([2,3,4],3)
    permutations(list(n), i + 1)
z=(permutations(list(n),1))
y=(permutations(list(n),2))

a= set()
a |= set(map(int, map("".join, permutations(list(n), 2))))
print(20**0.5)

print(list(permutations("ABCD",2)))
print(list(permutations(["A","B","C","D"],2)))
print("".join(['1','2','3']))
