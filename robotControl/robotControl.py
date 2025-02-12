'''
이 문제에서 정해야 할 것은, 
어디서 로봇을 꺾을(내려보낼)것이냐 다. 문제에서 탐사했던 지점은 다시 돌아가지 않는다는 문제 특성상, 
좌우로 왔다갔다 할 수 없고, 한번 내려온 층은 다음 내려가는 지역까지 직진을 하는 수 밖에 없다. 
뭔가 하나의 결정이 다음 결정에 영향을 끼치고 하는 느낌이 또 백트래킹의 냄새가 스멀스멀 난다. 
한줄에 최대 1000개, 그리고 그 선택이 또 1000개이니, 
브루탈로 풀자니 1000 ^ 999의 경우의 수다. 

논리적인 방향으로 그리디를 섞을수는 없을까?
이번 줄에서는 최대한 많이 먹고, 다음줄로 내려갈 때에는 손해를 최소화하는 그런 논리 말이다. 
뭔가 있을거 같다. 딱 2줄만 생각하고 진행하면 될거같은 그런 느낌 말이다. 
요컨대, 
현재의 줄 기준 가치, 
다음줄 기준 가치가 있다. 
현재의 줄은 무조건 양수면 통과, 음수라면 이걸 통과하는 것을 감수하고서라도 다음에 더 큰 양수가 있는가 정도이다. 
이때 다음 줄의 가치를 따지자면, 다음 먹는 양수가 있지만, 아래칸의 음수가 너무 크다면 먹을 가치가 없다. 
두줄만 보면 머리아프고, 누적적으로 따지자니 유턴을 안하고 그냥 음수밭을 가로질러서 최소한의 양수 낙하를 하는 등 경우의 수가 좀 많다. 
그렇다고 완탐의 느낌은 진짜 아닌거 같다. 이익 실현의 극대화라는 목표가 있다. 
몇수앞까지 봐야하냐 라고 물으면 확답은 안나오지만, 2줄만 보고 뭔가 될거 같은 그런게 있다. 
밥먹고 와서 알고리즘 종류를 확인해봐야겠다. 동적 내지는 그리디라고 믿는다. 동적이 맞았다. 제발 잘 해보자.

동적이면 어떤 순서로 문제를 확장 해나갈까?
1. 시작 지점, 행이 주어짐. 
하강 시 고려되야 할 요소는 - 
하강지점까지 요소의 합
하강 후 획득 가능한 합의 열.
이걸 출력하는걸로 시작해보자. 

'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
prev_start = 0
next_prev_start = 0
prev = []
end = float('inf')
answer=0
for i in range(N):
    lines = list(map(int,input().split()))
    moveCheck = 0
    moveCheck_partner = 0
    if prev == []:
        pass
    else:
        # print(f'we are dealing with starting{prev_start} and line {prev}')
        prev_sum =0
        next_prev_start = 0
        cur_sum = [0]*M
        
        for j in range(M):
            if i !=N-1:
                if prev_start<=j:
                    prev_sum=sum(prev[prev_start:j+1])
                    # cur_sum[j]=sum(lines[prev_start:j+1])
                else:
                    prev_sum=sum(prev[j:prev_start+1])
                    # cur_sum[j]=sum(lines[j:prev_start+1])
                for k in range(M):
                    if k<=j:
                        cur_sum[k]=sum(lines[k:j+1])
                    else:
                        cur_sum[k]=sum(lines[j:k+1])

                if prev_sum>moveCheck:
                    next_prev_start = j
                    moveCheck = max(moveCheck,prev_sum)
                    moveCheck_partner = cur_sum[j]
                elif prev_sum + cur_sum[j]>moveCheck+moveCheck_partner:
                    next_prev_start = j
                    moveCheck = max(moveCheck,prev_sum+cur_sum[j])
                    moveCheck_partner = cur_sum[j]
            else:
                finalSum = 0
                finalprevSum = 0
                if prev_start<=j:
                    finalprevSum=sum(prev[prev_start:j+1])
                else:
                    finalprevSum=sum(prev[j:prev_start+1])
                for k in range(M):
                    if k<=j:
                        finalSum=sum(lines[k:j+1])
                    else:
                        finalSum=sum(lines[j:k+1])
                
                # print(finalprevSum)
                # print(finalSum)
                if finalprevSum+finalSum>moveCheck:
                    next_prev_start = j
                    moveCheck = max(moveCheck,finalprevSum+finalSum)
                    # print(f'update with max val{moveCheck} at {j}')




            
    answerStart = min(prev_start,next_prev_start)
    answerEnd = max(prev_start,next_prev_start)
    answer+=sum(prev[answerStart:answerEnd+1])
    prev_start = next_prev_start
    # print(f'prev_start changed to {prev_start}, with subSum{answer}')
    if i == N-1:
        answer+=sum(lines[answerEnd-1:])
        print(answer)
    
    prev=lines[:]


