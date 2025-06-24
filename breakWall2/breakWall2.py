'''
[지금까지 움직인 칸 수, 부순 벽의 수, 현재 좌표, 입장한 방향.]
부순 벽의 수 < 주어진 K
입장한 방향으로 역주행 제외한 경우, 
역주행을 제외한 경우 칸이 존재한다면 업뎃, 

검증 후 넣었으면 함. 안그럼 쓸데없는 탐색이 늘어나니까.

2. 들어갈 새로운 데이터 생성
3. 데이터 검증(벽 부수기 가능, cost 업데이트 충족, 덜 부순 순으로 업뎃 등...) 시 새로운 힙 입력과 동시에 데이터 업데이트.

'''
import sys, heapq
input = sys.stdin.readline
N, M, K  = map(int,input().split())
mapList = []
dirs = [[0,1],[1,0],[0,-1],[-1,0]]
costMapList = [[[float('inf')for k in range(K+1)]for i in range(M)]for j in range(N)]
costInfoList = [[1,0,[0,0],-1]]
heapq.heapify(costInfoList)
for i in range(N):
    mapList.append(list(input().strip()))
while costInfoList:
    curInfo = heapq.heappop(costInfoList)
    cost = curInfo[0]
    hasBroke = curInfo[1]
    curPos = curInfo[2]
    dirFrom = curInfo[3]
    if dirFrom == -1:
        for i in range(2):
            dirsInfo = dirs[i]
            # dirRev = (dirFrom+2)%4
            # if i!=dirRev:
            newPos = [curPos[0]+dirsInfo[0],curPos[1]+dirsInfo[1]]
            if 0<=newPos[0]<N and 0<=newPos[1]<M:# 존재하는 위치이면서, 
                newCost = cost+1
                newDir = i
                if mapList[newPos[0]][newPos[1]] =='1':
                    newHasBroke =hasBroke + 1
                    if newHasBroke>K:
                        continue
                oldCost = costMapList[newPos[0]][newPos[1]][newHasBroke]
                if newCost < oldCost : 
                    costMapList[newPos[0]][newPos[1]][newHasBroke] = newCost
                    heapq.heappush(costInfoList,[newCost,newHasBroke,newPos,newDir])
                    if newPos==[N-1,M-1]:break
    else:
        for i in range(len(dirs)):
            dirsInfo = dirs[i]
            dirRev = (dirFrom+2)%4
            if i!=dirRev:
                newPos = [curPos[0]+dirsInfo[0],curPos[1]+dirsInfo[1]]
                if 0<=newPos[0]<N and 0<=newPos[1]<M:# 존재하는 위치이면서, 
                    newCost = cost+1
                    newDir = i
                    if mapList[newPos[0]][newPos[1]] =='1':
                        newHasBroke =hasBroke + 1
                        if newHasBroke>K:
                            continue
                    else:newHasBroke = hasBroke
                    oldCost = costMapList[newPos[0]][newPos[1]][newHasBroke]
                    if newCost < oldCost : 
                        costMapList[newPos[0]][newPos[1]][newHasBroke] = newCost
                        heapq.heappush(costInfoList,[newCost,newHasBroke,newPos,newDir])
                        if newPos==[N-1,M-1]:break

                    # if costMapList[newPos[0]][newPos[1]] # 목적지 정보(움직인 칸수, 부순 갯수)
if min(costMapList[-1][-1]) == float('inf'):
    print(-1)
else: print(min(costMapList[-1][-1]))

