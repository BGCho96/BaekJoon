import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())
answer=0
queenInfo = [-1] * N
# N - ans
"""
1 - 1
2 - 0 
3 - 0
4 - 0 - (4 * (4-3)) 
5 - 5 
귀찮고 경우의 수가 이쁘게 안떨어진다. 
백트래킹 될거같음
실제 방법도 그거임. 
지금까지의 방법을 복기하며 이번 백트래킹 구조를 생각해보자. 
행 간격의 경차와 열 간격의 경차는 동일하면 안된다. 
열 정보 중 중복은 있을 수 없다.
2개의 조건을 만족해야 하며 
def backtracking(depth, result, horses):
depth를 열 번호로, result를 갱신 정답 횟수로, 위치 정보를 horse로 해보자. 
"""
def check(colDepth):

    for row in range(colDepth):
        if queenInfo[colDepth] == queenInfo[row] or colDepth - row == abs(queenInfo[colDepth] - queenInfo[row]):
            return 0
    return 1

def backtrack(colDepth):
    global answer
    if colDepth==N:
        answer+=1

    else:
        for i in range(N):
            queenInfo[colDepth]=i
            if check(colDepth):
                backtrack(colDepth+1)

backtrack(0,[0 for i in range(N)])
print(answer)

# for j in combinations(range(N),2):
#     gap = abs(j[0]-j[1])
#     print(gap)



    
# import sys
# input = sys.stdin.readline

# n = int(input())
	
# visited = [-1] * n
# cnt = 0

# def check(now_row):
#     for row in range(now_row):
#         if visited[now_row] == visited[row] or now_row - row == abs(visited[now_row] - visited[row]):
#             return False
#     return True

# def dfs(row):
#     global cnt
    
#     if row == n: 
#         cnt += 1

#     else:
#         for col in range(n):
#             visited[row] = col
#             if check(row): 
#                 dfs(row + 1) 
                
# dfs(0)
# print(cnt)