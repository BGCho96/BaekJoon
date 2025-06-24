import sys
input = sys.stdin.readline
N = int(input())
timeCost  = []
profit = []
answer = 0
for i in range(N):
    time, cost = map(int,input().split())
    timeCost.append(time)
    profit.append(cost)
# print(timeCost, profit)
for i in range(2**N):
    scheduleCheck = [0 for j in range(N)]
    indicator = list(map(int,bin(i)[2:].zfill(N)))
    possible = 1
    for k in range(N): #N일간의 스케줄에서, 실행 가능한지 체크
        
        K = indicator[k]
        if K:

            for date in range(k,k+timeCost[k]):
                if date>=N:
                    possible = 0
                    break
                scheduleCheck[date]+=1


    # print('실행 일정')
    # print(indicator)
    # print('겹침 일정')
    # print(scheduleCheck)
    if max(scheduleCheck)>1: # 스케줄 중복시 끝
        possible =0
        continue
    # print('가능 여부')
    # print(possible)

    if possible:
        answer = max(answer,sum([profit[test] for test in range(N) if indicator[test]==1]))

print(answer)

