'''
이 문제는 다익스트라 변형이라고 생각된다. 
경로간선의 합이 아닌 새로운 간선 값과 이전 경로 값중 큰 값을 고르고, 기존의 값보다 작은지를 비교해서 입력하는 식으로. 
그렇다면, 
1. INF값을 큰 양수로 설정, 작은 값으로 업데이트하는 다익스트라 구현.  - 벌써 틀림. 두 값 중 큰걸 해야하니까 음의 큰 값임
2. 출발지 갯수만큼 다익스트라 행렬이 필요함. 다익스트라[출발지 번호] 따위의 꼴이 되겠다.
3. 2번에서 최솟값이 결정되면, 해당 노드에서 동일한 알고리즘 실행, 가장 값이 작은 출발지 값을 계산.
4. 2번과 3번에서 결정된 경로...는 합칠필요 없고 산봉우리 저장, 그리고 2번과 3번중에서 큰 값을 출력.

그럼 다익스트라를 어떻게 구현했었는지 기억을 더듬어 보자. 
1. 출발노드를 입력. 출발 노드의 인접값 모두 업데이트. 출발노드 방문처리.
2. 방문한적 없는 노드중에서 비용이 가작 작은 노드부터 방문, 인접노드 업데이트 반복.
필요한 변수로는 다익스트라 2차원 행렬.
모든 노드를 방문처리할때까지 while문 돌리는 구조. 이를 다익스트라 행렬 길이만큼 실행.


논리 단계 2번을 구현하고 나서, 의문이 들었다. 모든 출발지에서 모든 봉우리까지의 경로를 정했고, 가장 intensity가 낮은 값을 꼽았다.
그럼 해당 봉우리에서 내려오는데, 가장 낮은 intensity는 해당 출발지 아닌가...?이에 위배된다면, 해당 출발지와 봉우리 루트가 논리 2단계에서 선발되었겠지...?
일단은 이 논리로 제출해보자. 

경로를 넣어야 하나 말아야 하나 고민중이다. 산봉우리를 2번 넘으면 안된다는 룰이 추가되었다. 모오든 논리에 다 경로는 없었는데. 없이 어떻게 안되나....
산봉우리를 겪으면 float로 타입변경을 때려버릴까.근데 그럼 산봉우리를 찍는 하나의 경로가 너무나 가성비여서, 온갖 노드를 다 float로 물들이면,,,
어떡하지??이런 경우에 지켜져야 할 산봉우리나 노드가 있을까.
부정하고 싶은 마음 49퍼센트, 직관적으로 없다가 51퍼센트다. 
직관적으로, 진짜 정성들여 엿맥이는 케이스 말고는 다른 출발지에서 가까운 노드는 알아서 지켜질 것이다. 해보자.

시간도 초과되고 논리도 불완전하다.
'''
n = 7
paths = [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]]
gates = [3,7]
summits = [1, 5]	
def solution(n, paths, gates, summits):
    INF = int(10e9)

    costPerGates=[]
    connTable = [[-1 for i in range(n)]for j in range(n)]
    for s , e, c in paths:
        start = s-1
        end = e-1
        connTable[start][end] = c
        connTable[end][start] = c
    for gateNum in gates:
        temp = [[-1,{i}] for i in range(n)]
        temp[gateNum-1][0] = 0
        costPerGates.append(temp)
    for i in range(len(gates)):
        visited = [nodes for nodes in range(n)]
        curNode=gates[i]-1
        while visited:
            visited.remove(curNode)
            for cango in range(len(connTable[curNode])):
                if connTable[curNode][cango] >0:
                    newCost = connTable[curNode][cango]
                    if cango in visited:
                        # if costPerGates[i][curNode][0]<=newCost:
                        #     costPerGates[i][cango][0] = newCost
                        #     costPerGates[i][cango][1].add(curNode)
                        #     for history in costPerGates[i][curNode][1]:
                        #         costPerGates[i][cango][1].add(history)
                        costPerGates[i][cango][0] = max(costPerGates[i][curNode][0],newCost)
                        
            nextNodeHint = INF
            for j in visited:
                if costPerGates[i][j][0]<nextNodeHint and costPerGates[i][j][0]>0:
                    nextNodeHint = costPerGates[i][j][0]
                    curNode = j
    intensityHint = INF
    top = -1
    for i in range(len(costPerGates)):
        for j in summits:
            topNum = j-1
            if costPerGates[i][topNum][0]<intensityHint:
                # count = 0
                # for check in  costPerGates[i][topNum][1]:
                #     if check+1 in summits:
                #         count+=1
                # if count<2:
                top = topNum+1
                intensityHint = costPerGates[i][topNum][0]

            
            
    answer = [top,intensityHint]
    return answer
solution(n, paths, gates, summits)