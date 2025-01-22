import sys
input = sys.stdin.readline
answer=0
comNum, lineNo = map(int, input().split())
connetionInfo = [[0 for i in range(comNum)]for i in range(comNum)]

for i in range(lineNo):
    start, end, cost = map(int, input().split())

    connetionInfo[start-1][end-1] = cost
    connetionInfo[end-1][start-1] = cost

V1,V2 = map(int,input().split())
costTableFrom0 = [int(10e9) for i in range(comNum)]
costTableFromV1 = [int(10e9) for i in range(comNum)]
costTableFromV2 = [int(10e9) for i in range(comNum)]
costTableFrom0[0]=0
costTableFromV1[V1-1]=0
costTableFromV2[V2-1]=0
routeTable = [[]for i in range(comNum)]
visited = [i+1 for i in range(comNum)]
currentNode0List = []
currentNode0List=[visited.pop(0)]
# pastNode = -1
while currentNode0List:
    # if costTableFrom0 == pastNode:
    #     break
    currentNode0=currentNode0List.pop(0)
    routCost = connetionInfo[currentNode0-1]
    for target in range(comNum):
        if routCost[target] !=0:
            if costTableFrom0[currentNode0-1] + routCost[target] < costTableFrom0[target]:
                costTableFrom0[target] = costTableFrom0[currentNode0-1] + routCost[target]
                currentNode0List.append(target+1)
                if target+1 in visited:
                    visited.remove(target+1)
    
    if currentNode0List == []:
        if visited:
            currentNode0List.append(visited.pop(0))

visited = [i+1 for i in range(comNum)]
currentNodeV1List = []
currentNodeV1List=[visited.pop(0)]
# pastNode = -1
while currentNodeV1List:
    # if costTableFrom0 == pastNode:
    #     break
    currentNodeV1=currentNodeV1List.pop(0)
    routCost = connetionInfo[currentNodeV1-1]
    for target in range(comNum):
        if routCost[target] !=0:
            if costTableFromV1[currentNodeV1-1] + routCost[target] < costTableFromV1[target]:
                costTableFromV1[target] = costTableFromV1[currentNodeV1-1] + routCost[target]
                currentNodeV1List.append(target+1)
                if target+1 in visited:
                    visited.remove(target+1)
    
    if currentNodeV1List == []:
        if visited:
            currentNodeV1List.append(visited.pop(0))
    # pastNodeV1 = costTableFromV2
visited = [i+1 for i in range(comNum)]
currentNodeV2List = []
currentNodeV2List=[visited.pop(0)]
# pastNode = -1
while currentNodeV2List:
    # if costTableFrom0 == pastNode:
    #     break
    currentNodeV2=currentNodeV2List.pop(0)
    routCost = connetionInfo[currentNodeV2-1]
    for target in range(comNum):
        if routCost[target] !=0:
            if costTableFromV2[currentNodeV2-1] + routCost[target] < costTableFromV2[target]:
                costTableFromV2[target] = costTableFromV2[currentNodeV2-1] + routCost[target]
                currentNodeV2List.append(target+1)
                if target+1 in visited:
                    visited.remove(target+1)
    
    if currentNodeV2List == []:
        if visited:
            currentNodeV2List.append(visited.pop(0))
    # pastNodeV2 = costTableFromV2
route1 = costTableFrom0[V1-1] + costTableFromV1[V2-1] + costTableFromV2[comNum-1]
route2 = costTableFrom0[V2-1] + costTableFromV2[V1-1] + costTableFromV1[comNum-1]

answer=min(route1,route2)
if answer >= int(10e9):
    print(-1)
else: print(answer)

    