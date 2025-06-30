'''
뱀 문제와 유사하게, 문제를 구현할 필요없이 필요 요소만 구현하면 되지 싶다. 
톱니바퀴의 상태만 저장하고, 축상에 있는 톱니의 이빨 위치를 저장하고자 한다
요컨대, 12시부터 데이터를 입력시켜주니까 초기값은 7번째 위치를 Head(축상에서 왼쪽 끝 위치)로 지정하면, 자연스레 
(Head+4)%8의 값으로 Tail(축상 오른쪽 끝 위치)를 지정 가능할거다. 
GearInfo[][] 고정값, 변화하는 HeadInfo[]를 업데이트하는 방법으로 진행하면 되지 싶다.

이제 약간 어려운 부분은, 몇번 톱니를 돌릴때 어떤 톱니를 돌리느냐의 구현 방법이겠다.

기본 골자는, 
spin(GearNo, Dir)일텐데, 
4개의 케이스를 다 찢느냐, 아니면 나름의 논리로 통합형 솔루션을 제시하느냐 정도이겠다.
통합적인 접근도 가능할거 같다. 톱니의 갯수가 유동적인 상황에 적용 가능한 수준으로 말이다.
1. 톱니가 바로 옆 톱니를 움직이느냐를 head, tail로 알 수 있다.
2. 그럼 일명, '같이 묶인'톱니 그룹을 규정할 수 있다.
예를 들어, [[1,2],[3,4]]
이런 식으로 말이다. 바꾸려는 톱니가 포함된 그룹이 나올때까지 묶인 그룹을 돌리면 어떤 톱니들이 돌게 되는건지 알게 되는 것이다.
그렇다면 그룹화 함수도 만들면 좋지 않을까?
curGearGroup = setGearGroup()
이런 식으로?
for commandNum:
    commandInfo[i]
    curGearGroup = setGearGroup()
    for groups in curGearGroup:
        if commandInfo[i][0] in curGearGroup:
            그룹 선정
    spin()
'''
import sys
input = sys.stdin.readline
gearInfo = []
commandInfo = []
headInfo = [6 for i in range(4)]
def spin(gearNo, dir, gearGroup):
    if dir == 1:
        shiftVal = -1
    else:
        shiftVal = 1
    headInfo[gearNo] = (headInfo[gearNo] + shiftVal) % 8
    newShiftVal = shiftVal
    for i in range(gearNo,gearGroup[-1]+1):
        if i == gearNo:
            continue
        newShiftVal *= -1
        headInfo[i] = (headInfo[i] + newShiftVal) % 8
    newShiftVal = shiftVal
    for i in range(gearNo,gearGroup[0]-1,-1):
        if i == gearNo:
            continue
        newShiftVal *= -1
        headInfo[i] = (headInfo[i] + newShiftVal) % 8
    return 0
def setGearGroup():
    gears = [i for i in range(4)]
    group = []
    underGroup = []
    for i in gears:
        if i == 0:
            underGroup.append(i)
        else:
            if gearInfo[i][headInfo[i]] != gearInfo[i-1][(headInfo[i-1]+4)%8]:
                underGroup.append(i)
            else:
                group.append(underGroup)
                underGroup=[]
                underGroup.append(i)
    group.append(underGroup)
    return group
for i in range(4):
    gearInfo.append(list(map(int,input().strip())))
# print(gearInfo)
commandNum = int(input())
# print(commandNum)
for i in range(commandNum):
    commandInfo.append(list(map(int,(input().strip().split(' ')))))
# print(commandInfo)
# print(setGearGroup())


for i in range(commandNum):
    targetGear = commandInfo[i][0]-1
    commandType = commandInfo[i][1]
    groupSet = setGearGroup()
    for groups in groupSet:
        if targetGear in groups:
            targetGroup = groups[:]
    # print(f'바꾸려는 기어, 바꾸려는 방향{targetGear,commandType}')
    # print(f'바꾸기 전,{headInfo}')
    spin(targetGear, commandType, targetGroup)
    # print(f'바꾸기 전후,{headInfo}')
print(int(''.join([str(gearInfo[i][(headInfo[i] + 2) % 8]) for i in range(4)])[::-1],2))