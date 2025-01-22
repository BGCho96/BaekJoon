import sys
from math import inf
input = sys.stdin.readline

numNodes, numRoutes = map(int,input().split())
connectionInfo =[[inf for k in range(numNodes)]for j in range(numNodes)]
for routeNo in range(numRoutes):
    start, end, cost = map(int,input().split())
    connectionInfo[start-1][end-1]=min(connectionInfo[start-1][end-1],cost)
    connectionInfo[end-1][start-1]=min(connectionInfo[end-1][start-1],cost)
    

for interNode in range(numNodes):
    connectionInfo[interNode][interNode]=0
    for startNode in range(numNodes):
        for endNode in range(numNodes):
            newnewCost = connectionInfo[startNode][interNode]+connectionInfo[interNode][endNode]
            connectionInfo[startNode][endNode] = min(connectionInfo[startNode][endNode],newnewCost)

# for factor in (connectionInfo):
#     print(factor)
J, S = map(int,input().split())
answer=-1
costSum = inf
cand=[]
for i in range(numNodes):
    Jcost = connectionInfo[i][J-1]
    Scost = connectionInfo[i][S-1]
    if i+1 == J or i+1 == S : #1번조건과 
        continue
    newCost = Jcost + Scost
    if newCost < costSum : # 2번조건 - 최소임을 보장해야 함
        costSum = newCost
        cand=[]
    if newCost == costSum :
        if Jcost<=Scost: # 3번조건, J 가 더 크면 걸러야 함
            cand.append([i+1,Jcost])
if cand:
    answer=sorted(cand,key=lambda x : (x[1],x[0]))[0][0]
print(answer)
