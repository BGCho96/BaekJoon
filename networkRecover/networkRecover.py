import sys
input = sys.stdin.readline
comNum, lineNo = map(int, input().split())
connetionInfo = [[0 for i in range(comNum)]for i in range(comNum)]

for i in range(lineNo):
    start, end, cost = map(int, input().split())
    connetionInfo[start-1][end-1] = cost
    connetionInfo[end-1][start-1] = cost
visited = [i+1 for i in range(comNum)]
costTable = [int(10e9) for i in range(comNum)]
costTable[0]=0
routeTable = [[]for i in range(comNum)]
currentNode = visited.pop(0)
while visited:
    routCost = connetionInfo[currentNode-1]
    for target in range(comNum):
        if routCost[target] !=0:
            if costTable[currentNode-1] + routCost[target] < costTable[target]:
                costTable[target] = costTable[currentNode-1] + routCost[target]
                newRoute = routeTable[currentNode-1][:]
                newRoute.append([currentNode,target+1])
                routeTable[target]=newRoute
    minFind = -1
    minFindVal=int(10e9)
    for i in visited:
        if costTable[i-1]<minFindVal:
            minFind=i
            minFindVal=costTable[i-1]
    if minFind!=-1:
        currentNode = minFind
        visited.remove(currentNode)

routeTable.pop(0)
answer=set()
for candidates in routeTable:
    for a,b in candidates:
        prepareSort=[a,b]
        prepareSort.sort()
        answer.add(tuple(map(str,prepareSort)))
print(len(answer))
for ans in answer:
    print(' '.join(ans))
    