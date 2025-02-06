'''
아주 전형적이고 만난적 있는 벨만 - 포드 방법이다. 
코드를 그냥 가져다와서 쓰고 싶지만, 복기도 할 겸 코테중이라고 이미지 트레이닝 할 겸 처음부터 짜보자. 
0. 입력갯수가 엄청 많아질수 있는 문제다. sys input 잘 쓸것
1. 간선 정보를 v-1만큼 돌리고, v만큼 돌렸을 때에 변화값이 있는지 확인하는 논리다
2. 이번에는 경로정보도 입력해야 한다. 간선 업데이트가 일어날 경우, 경로까지 저장해야 하니 값 + 문자열 논리를 써보자
순간 문제 읽다가 단어가 이상해서 놀랄뻔했다. 골목길이 교차하는 지점 갯수 - v랑 같은 말이다 쫄지 말자
골목길의 갯수 - 간선 수 . 사람 놀라게 하고 있다. 

문제가 생겼다. 생각지도 못한 시간초과... 왜 나는걸까?
벨만 포드가 내가 아는 이 방법 맞을텐데.(오늘 힌트 실수로 미리 봄)

일단 '유리하다' 라는 말이 참 마음에 안든다. 0의 경우 수가 무한히 흩뿌려져 있는 경우라면, 소득 없이 뺑뺑 도는 경우도 있다. 이러면 더 짧은걸 골라야 하나?
같을때는 업데이트 안한다 이렇게 가야하나? 그럼 그냥 처음에 발견된 경우만 남는다. 
일단 마주한 경우가 시간초과인 점 과 뭔가 묘하게 알던 벨만-포드랑 다른거 같아서 심란해진다. 
바보같이 반복횟수를 V대신 N을 넣었다. 생각하며 살 것.

문제를 잘 읽자 - 최적의 경로가 여러개면 아무거나 출력해라. 최적의 여부는 유일성의 여부가 아님.
76퍼센트 정도에서 논리 오류가 생겼다. 시간초과는 아니고, 금품이 최대화된다 의 논리가 위배된다는건데....흐음....

혹시나 해서 뺑뺑이를 극한으로 돈다고 생각해서 음수 최대치를 늘려도 안된다. 
벨만 포드 이외의 방법, 혹은 논리의 구멍이 뭐가 있을 수 있지??
딱 하나만 고심해서 질문 하나만 참고하자

진짜 통수를 얼얼하게 만드는 케이스다. 왜 이전 문제에는 이런 경우가 없었지???
타임머신이었던거 같은데, 해당 문제는 음의 사이클이 있는지만 판별한다. 
최대한 과거로 가는게 문제니까, 이 문제로 치면 억만장자가 될수 있는가 문제지, 이것과 도착 여부를 연관짓지 않았다. 하지만 이 문제는 도착하는 경우가 있냐고 묻고 있다. 
그러니까 이 문제는, V-1경우를 초과했을때, 도착지 값이 변화하느냐를 봐야하는거다!

제출하기 전에 한번만 고민해보자 도착지에 의미없는 루프가 있다면...?요컨대 00000같은걸로 경로만 축내는...?이득을 보는 경우가 아니니까 상관 없나...?
나의 개인적인 견해는 최단경로 선택을 넣어야 한다. 그래야 이득 없는데 헛도는 경우가 없으니까. 
최단경로를 제외하고 제출 해보고, 틀리면 내 방법을 넣어보자. 

둘다 틀렸다. 써글것.

제대로 이해한건지 모르겠다. 
"무한한 돈벼락 루트 존재" 와 "이를 이용하지 않는 루트 존재" 가 동시에 충족되어도 -1을 뱉어야 하는 느낌이다. 
이론상 무한한게 이득을 취하면서 도착도 할 수 있기에, "최대값"은 존재하지 않게 된다. 그러면서 이 외에 루트로 도착은 하지만, 이는 최대값을 충족시키지 못한다...
느낌인거 같다. 
그럼 무한루트 존재 + 이가 도착지로도 이어져 있을 경우를 식별해야 한다는거다. 


머리가 좀 아프니, 경우의 수를 정리해보자. 

1. 고전적인 벨만 - 포드로 풀리는 경우
2. 무한양/무한음 루트가 존재하지만, 이가 최적경로와 완전히 상관없는 경우
3. 무한양/무한음 루트와 고정수 루트가 동시에 존재하는 경우. 

3번 너무 골때린다... 어떻게 해야 분리가 가능하지?? 사실상 2번의 무한음 루트도 목적지 루트가 수정되지 않는다는 전제로 진행해버렸다. 
v번째를 돌리면 업데이트 되는놈이 있을거다. 얘가 목적지까지의 연결이 되어있는가...를 확인하는 것이 코드적으로 가능할까?
해봐야한다.


'''
import sys
input = sys.stdin.readline
V, N = map(int, input().split())
routInfo=[]
NegINF = int(-10e12)
for n in range(N):
    routInfo.append(list( map(int,input().split())))
costInfo = [[NegINF, []]for i in range(V)]
costInfo[0]=[0,[1]]
connInfo = [[0 for i in range(V)] for i in range(V)]

flag = 0
MegaRichLand = -1
for v in range(V):
    for s, e, c in routInfo:
        
        start = s-1
        end = e-1
        connInfo[start][end] =1
        if costInfo[start][0]!=NegINF and (costInfo[start][0]+c>costInfo[end][0]):
            costInfo[end] = [costInfo[start][0]+c,costInfo[start][1]+[e]]
            if v == V-1:
                MegaRichLand = end
            
        elif costInfo[start][0]!=-1 and (costInfo[start][0]+c==costInfo[end][0]):
            if len(costInfo[end][1])>len(costInfo[start][1])+1:
                costInfo[end] = [costInfo[start][0]+c,costInfo[start][1]+[e]]
                if v == V-1:
                    MegaRichLand = end

    if v == V-2:
        snapShot = costInfo[-1]
    if v == V-1 and snapShot != costInfo[-1]:
        flag = 1
MegaRichLandCanGo =[]
if MegaRichLand != -1:
    for v in range(V):
        if V-1 in MegaRichLandCanGo:
            flag = 1
            break
        nextHeading= []
        if v ==0:
            MegaRichLandCanGo = [MegaRichLand]
        for goto in MegaRichLandCanGo:
            for toward in range(len(connInfo[goto])):
                if connInfo[goto][toward] == 1: 
                    nextHeading.append(toward)
        MegaRichLandCanGo = nextHeading


if costInfo[-1][1]==[]:
    flag =1
if flag:
    print(-1)
else:
    print(' '.join(map(str,(costInfo[-1][1]))))