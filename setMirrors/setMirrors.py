'''
월요일날 했던 챌린지 문제랑 굉장히 흡사한거 같다. 
직진할때는 코스트가 없고, 
꺾을때만 값이 생기니까. 그럼 비슷한 원리로, 어떤 값이 어디서 들어올 때 얼마인지, 4개짜리 배열을 만들어서 다익스트라스러운 진행을 해보자.
일단 답변을 참고하기 전에.... 어떻게 했었는지 상기를 해보자. 
크기가 4짜리 배열을 힙에 어떤 형태로 넣었더라....?
힙에 들어갈 구조 정도만 생각해보자 . 
[비용, 좌표, 방향]
비용이라 함은 거울의 갯수가 될 것이고, 방향은 0123로 하고, 벽에 부딛히면 소멸하는걸로.
거울을 설치할수 없으면 비용 방향 유지한채로 좌표만 업데이트해서 다시 넣고.
딱히 문의 위치와 발사 방향에 대한 언급이 없으니까...먼저 발견한 문에서 사방으로 발사하는걸로.!
'''
import sys
import heapq
input = sys.stdin.readline
N = int(input())
mirrorBoard = []
costBoard = []
doorIndex = []
heapStack = []
for n in range(N):
    wallInfo = list(input().strip())
    mirrorBoard.append(wallInfo)
    costBoard.append([[float('inf')for j in range(4)] for i in range(len(wallInfo))])
    if '#' in wallInfo:
        for door in range(len(wallInfo)):
            if wallInfo[door] == '#':
                doorIndex.append([door,n])
firstDoorX, firstDoorY = doorIndex[0][0],doorIndex[0][1]
endDoorX,endDoorY = doorIndex[1][0],doorIndex[1][1]
direction = [i for i in range(4)]# 0 - up, 1 - right, 2 - down, 3 - left @@@@toward dir
costBoard[firstDoorY][firstDoorX] = [0,0,0,0]
leaved = 0
heapStack.append([0,[firstDoorY,firstDoorX],None])
while heapStack: 
    curCost, curCordinate, dirToward = heapq.heappop(heapStack)
    curCordinateY, curCordinateX = curCordinate[0],curCordinate[1]
    # prevCost = costBoard[curCordinateX][curCordinateY][dirToward]
    if mirrorBoard[curCordinateY][curCordinateX] == '#': # 문 도착
        if leaved == 0:
            nextDirs = [i for i in range(4)]
            for dirs in nextDirs:
                if dirs == 0:
                    nextCordinate = [curCordinate[0]+1,curCordinate[1]]
                if dirs == 1:
                    nextCordinate = [curCordinate[0],curCordinate[1]+1]
                if dirs == 2:
                    nextCordinate = [curCordinate[0]-1,curCordinate[1]]
                if dirs == 3:
                    nextCordinate = [curCordinate[0],curCordinate[1]-1]

                if (0<=nextCordinate[0]<N) and (0<=nextCordinate[1]<N):
                    prevCost = costBoard[nextCordinate[0]][nextCordinate[1]][dirs]
                    if curCost < prevCost:
                        costBoard[nextCordinate[0]][nextCordinate[1]][dirs] = curCost
                        heapq.heappush(heapStack,[curCost,nextCordinate,dirs])
            leaved = 1
        else:
            break
    elif mirrorBoard[curCordinateY][curCordinateX] == '.': # 설치 불가, 그대로 통과 .들어온 들어온 방향의 값만 갱신. 갱신 시에만 HEAP에 입력
        # prevCost = costBoard[curCordinateX][curCordinateY][dirToward]
        if dirToward == 0:
            nextCordinate = [curCordinate[0]+1,curCordinate[1]]
        if dirToward == 1:
            nextCordinate = [curCordinate[0],curCordinate[1]+1]
        if dirToward == 2:
            nextCordinate = [curCordinate[0]-1,curCordinate[1]]
        if dirToward == 3:
            nextCordinate = [curCordinate[0],curCordinate[1]-1]
        if (0<=nextCordinate[0]<N) and (0<=nextCordinate[1]<N):
            prevCost = costBoard[nextCordinate[0]][nextCordinate[1]][dirToward]
            if curCost < prevCost:
                costBoard[nextCordinate[0]][nextCordinate[1]][dirToward] = curCost
                heapq.heappush(heapStack,[curCost,nextCordinate,dirToward])
    elif mirrorBoard[curCordinateY][curCordinateX] == '!': # 설치 가능. 4방향...으로 쏠거까지는 없고, 3방향으로 쏘고, 좌우(수직)의 경우에만 cost 증가, 직진은 ! 논리로 구현
        nextDirs = [i for i in range(4) if i != (dirToward+2)%4]
        for dirs in nextDirs:
            if dirs == 0:
                nextCordinate = [curCordinate[0]+1,curCordinate[1]]
            if dirs == 1:
                nextCordinate = [curCordinate[0],curCordinate[1]+1]
            if dirs == 2:
                nextCordinate = [curCordinate[0]-1,curCordinate[1]]
            if dirs == 3:
                nextCordinate = [curCordinate[0],curCordinate[1]-1]
            if (0<=nextCordinate[0]<N) and (0<=nextCordinate[1]<N):
                prevCost = costBoard[nextCordinate[0]][nextCordinate[1]][dirs]

                if dirs == dirToward:
                    if curCost < prevCost and (0<=nextCordinate[0]<N) and (0<=nextCordinate[1]<N):
                        costBoard[nextCordinate[0]][nextCordinate[1]][dirToward] = curCost
                        heapq.heappush(heapStack,[curCost,nextCordinate,dirToward])
                else:
                    newCurCost = curCost+1
                    if newCurCost < prevCost and (0<=nextCordinate[0]<N) and (0<=nextCordinate[1]<N):
                        costBoard[nextCordinate[0]][nextCordinate[1]][dirs] = newCurCost
                        heapq.heappush(heapStack,[newCurCost,nextCordinate,dirs])

print(min(costBoard[endDoorY][endDoorX]))
