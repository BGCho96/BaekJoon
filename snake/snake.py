'''
1. 맵 구현
2. 뱀의 진행 방법, 소멸 방법 정하기
2-1. 이중 큐.
방향에 따라 한쪽 끝에 머리 추가, 사과가 없다면 반대쪽 삭제.
2-2. 실패 조건
벽 내지는 자기 자신에 부딪히면 게임 오버. 
추가하려는 칸이 칸 크기보다 크거나, 몸 안에 있으면 게임 오버.
함수(몸, 크기 N, 방향)을 통해서 다음 칸이 유효한지 구현해야 함.
2-3. 진행 방향
오른쪽 왼쪽 회전으로 주어졌기에, 상, 우, 하, 좌 를 하나의 리스트에 넣고, 오른쪽과 왼쪽 회전 시에 상태값이 더하거나 빼거나로 상태 결정
처음 값이 오른쪽으로 보는 것이니까, [우, 하, 좌, 상]으로 하고 첫 상태값을 0으로 설정하는 것이 바람직하다.

====================
ver1
맵 선언, body 리스트로 작성-dequeue 찾아봐서 시간 복잡도 찾아보고 유리하다 싶으면 적용

무조건 시간이 지나고, 움직이고 게임 오버가 결정되니, 시간 + 하고 결과 탐색

'''

import sys
input = sys.stdin.readline
N = int(input())
numApple = int(input())
appleInfo = []
for i in range(numApple):
    appleX, appleY = map(int,input().split())
    appleInfo.append([appleY-1, appleX-1])
numDirChange = int(input())
dirChangeInfo = []
for i in range(numDirChange):
    temp = list(input().split())
    dirTime = int(temp[0])
    dirType = temp[1]
    dirChangeInfo.append([dirTime,dirType])
# print(N,numApple,appleInfo,numDirChange,dirChangeInfo)

'''
생각해보니 맵을 구현할 필요가 없다. 가상진행을 시뮬레이션 해보자.
while gameover:
구조 안에서 시간 증가.
if command 등으로 커맨드 시작. 

domap의 결과물은 뭐가 필요할까?
domap(body, dirStatus[dirIndex],N) 의 형태가 출력해야 할 것은, 
body의 새로운 형태만 있으면 되나...? 출력값 없이...?
1. body - 호출만으로 값 변경 완료
2. 사과값 - 호출만으로 값 변경 가능함.
3. 게임오버 여부 정도나 리턴값으로 주면 될려나...?

'''
def domap(bodyDeque, dirToGo, mapSize):
    done = 0
    head = bodyDeque[0]
    nextHead = head[:]
    if dirToGo == 'up':
        nextHead[1] -= 1
    if dirToGo == 'down':
        nextHead[1] += 1
    if dirToGo == 'right':
        nextHead[0] += 1
    if dirToGo == 'left':
        nextHead[0] -= 1
    
    if max(nextHead)>=N or min(nextHead)<0:
        done = 1
    elif nextHead in bodyDeque:
        done = 1
    else:
        bodyDeque.appendleft(nextHead)
    
    if nextHead in appleInfo:
        appleInfo.remove(nextHead)
    else:
        bodyDeque.pop()

    return done
from collections import deque
body = deque()
body.append([0,0])
currCommand = dirChangeInfo.pop(0)
gameover = 0
time = 0
dirIndex = 0
dirStatus = ['right', 'down', 'left', 'up']
while not gameover:
    time += 1
    gameover = domap(body, dirStatus[dirIndex],N)
    if time == currCommand[0]:
        if currCommand[1] == 'D':
            dirIndex+=1
            dirIndex%=4
        if currCommand[1] == 'L':
            dirIndex-=1
            dirIndex%=4
        if dirChangeInfo:
            currCommand = dirChangeInfo.pop(0)
        else:
            currCommand = [None,None]
    
print(time)

