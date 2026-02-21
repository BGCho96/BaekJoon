import sys
input = sys.stdin.readline
inf = 10e9
# def rootOut(node):
#     if prevInfo[node] == -inf:
#         return node
#     else: return rootOut(prevInfo[node])
# def tailOut(node):
#     while tailInfo[node] != node:
#         node = tailInfo[node]
#     return node
N = int(input())
answer=[]
nameSack = []
lastTailInfo = [i for i in range(N)]
nextInfo = [i for i in range(N)]
# tailInfo = [i for i in range(N)]
degree = [0]*N

for k in range(N):
    nameSack.append(input().strip())
# print(nameSack)
for k in range(N-1):
    i, j = map(int,input().split())
    t = lastTailInfo[i-1]
    nextInfo[t] = j-1
    # lastTailInfo[t] = j-1
    lastTailInfo[i-1] = lastTailInfo[j-1]
    degree[j-1]+=1
for i in range(len(degree)):
    if degree[i] == 0:
        start = i
        break
# print(lastTailInfo)
# print(nextInfo)
# print(degree)
# print(nextInfo)

# print(nextPos)
nextPos = start
while True:
    answer.append(nameSack[nextPos])
    if nextInfo[nextPos] == nextPos:  # 다음이 자기 자신 → 끝
        break
    nextPos = nextInfo[nextPos]
    
print(''.join(answer))
