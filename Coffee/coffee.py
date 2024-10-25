N, K = map(int, input().split())
if K==0:
    print(0)
caffeine_vol=list(map(int, input().split()))
if min(caffeine_vol)>K:
    print(-1)

# print(caffeine_vol)
status=[[[0,0]for i in range(N)]]
min_cup=N
found=0
for n in range(1,K+1):
    status_N=[]
    candidate_K=[K+1,N]
    for k in range(len(caffeine_vol)):
        status_K=[]
        if n==1 and n-caffeine_vol[k]>=0:# 첫잔일 경우, 잔여 배부름만 고려
            status_K=[n-caffeine_vol[k],1]
        else:
            if n-caffeine_vol[k]>=0: # 첫잔이 아니라면, 잔여 용량을 봐야하므로, 한잔을 추가했을 경우의 상태를 관찰한다
                if k!=0:
                    newCoffee=[n-caffeine_vol[k]-(n-caffeine_vol[k]-status[n-caffeine_vol[k]][k-1][0]),status[n-caffeine_vol[k]][k-1][1]+1]#k=1번째 커피를 마신다면?
                    if newCoffee[0]<status_N[-1][0]: # 마셨을 때 카페인 이득이 있다면, 이 상태로 치환                    
                        status_K=newCoffee
                    elif newCoffee[0]==status_N[-1][0] and newCoffee[1]<status_N[-1][1]:# 잔수 이득만 있음
                        status_K=newCoffee
                    else:#마셔봤자 카페인 총량에 이득이 없는 경우
                        if k!=1:
                            status_K=status_N[-1]
                        else:
                            status_K=[status[n-1][k-1][0]+1,status[n-1][k-1][1]] #용량 고려시, 이 잔을 마시는 것이 불가능. 
                else:status_K=[n-caffeine_vol[k],1]
            else: # 마실수가 없는 상태
                if n!=1:
                    if status_N:
                        status_K=status_N[-1]
                    else:status_K=[n,0]
                else:
                    if n==1:
                        status_K=[n,0]
                    else:status_K=status_K=[status[n-1][k-1][0]+1,status[n-1][k-1][1]] #용량 고려시, 이 잔을 마시는 것이 불가능. 

                
        if status_K[0]<=candidate_K[0]:
            if status_K[1]<candidate_K[1]:
                candidate_K=status_K
        else:
            if k!=0:
                status_K=status_N[-1]
            else:
                status_K=status[n-1][k-1]

        if n==K and status_K[0]==0 and status_K[1]<min_cup:
            found=1
            min_cup=status_K[1]
        status_N.append(status_K)
    status.append(status_N)
print(caffeine_vol)
for line in status:
    print(line)

if not found:
    print(-1)
else:print(min_cup)
