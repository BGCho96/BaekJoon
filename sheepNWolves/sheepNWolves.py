
# 이 버전의 문제에 대입하자면, depth는 없고(정해진 갈림길의 한계가 없음으로), result는 양과 늑대의 수, horses는 여태 만든 선택지의 결과 아닐까?
# 업데이트해야할 정보는 무엇이 있을까? 종료 정보는?
# 주사위를 10개 던져야 끝나는게 전 상황이었다면, 이제는 다음 후보지가 없거나, 늑대를 더 주울수 없는데 늑대밖에 없을 때인거 같다. 

# 지금까지 선택의 번호 list, choices []
# 늑대와 양의 숫자 비율 list, sheepNWolves []
# choices에 따라 정해지기는 하지만, 다음 선택지들의 목록, list nextNodes []
# 초기값, [0], [1,0],nodeInfo[0][1]
answer = 0
maxSheep = 0
def solution(info, edges):
    global maxSheep
    maxSheep = len(info)-sum(info)
    nodeInfo = dict()
    for i in range(len(info)):
        nodeInfo[i] = [info[i],[]]
    for parent, son in edges:
        nodeInfo[parent][1].append(son)
    # print(nodeInfo)
    backtracking([0],[1,0],nodeInfo[0][1],nodeInfo)
    return answer
def backtracking(choices, sheepNWolves, nextNodes,nodeInfo):
    global answer
    global maxSheep
    if answer==maxSheep:
        return
    animalCheck = [nodeInfo[i][0] for i in nextNodes]
    if nextNodes == [] or (sheepNWolves[0]-sheepNWolves[1]==1  and 0 not in animalCheck):
        # answer = max(answer, result)
        answer = max(answer,sheepNWolves[0])
        return
    
    for i in range(len(nextNodes)):
        # 하나의 선택지를 선택하면, 늑대가 더 많아지는게 아니라면, 선택지를 갱신하고 다음 선택을 강행한다. 
        choiceInfo = nodeInfo[nextNodes[i]]
        moreWolves = sheepNWolves[:]
        moreWolves[nodeInfo[nextNodes[i]][0]]+=1
        
        nextChoice = nextNodes[:]
        nextChoice.pop(i)
        nextChoiceList = choices[:]
        nextChoiceList.append(nextNodes[i])
        for j in reversed(choiceInfo[1]):
            nextChoice.insert(i,j)
        
        if moreWolves[0]>moreWolves[1]:
            
            backtracking(nextChoiceList, moreWolves, nextChoice,nodeInfo)
    
info = [0,1,0,1,1,0,1,0,0,1,0]
edges =[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
solution(info, edges)
print(answer)



#     for i in range(4):
#         # 현재 말 위치
#         x = horses[i]

#         # 현재 말 위치가 2갈래 갈 수 있는 위치(10, 20, 30)인지 체크
#         if len(graph[x]) == 2:
#             # 파란 길 한 칸 진입
#             x = graph[x][1]
#         else:
#             # 빨간 길 한 칸 진입
#             x = graph[x][0]

#         # 나온 주사위 값 만큼 말 이동(위에서 1칸 이동했기 때문에 1 덜 이동함)
#         for _ in range(1, diceInfo[depth]):
#             x = graph[x][0]

#         # 목적지에 도착했거나 or (아직 목적지가 아니고 and 거기에 말이 없다면)
#         if x == 32 or (x < 32 and x not in horses):
#             before = horses[i]  # 이전 말의 위치
#             horses[i] = x  # 현재 말 위치 갱신

#             backtracking(depth + 1, result + score[x], horses)

#             horses[i] = before


# backtracking(0, 0, [0, 0, 0, 0])

info = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16]]
Return = 17