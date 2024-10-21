N, K = map(int, input().split())
caffeine_vol=list(map(int, input().split()))
print(caffeine_vol)
status=[[[0,0]for i in range(K)]]
for n in range(1,N):

    status_N=[]
    candidate_K=[K+1,N]
    for k in caffeine_vol:
        status_K=[]
        if n==1 and n-k>=0:# 첫잔일 경우, 잔여 배부름만 고려
            status_K=[n-k,1]
        else:
            if n-k>=0: # 첫잔이 아니라면, 잔여 용량을 봐야하므로, 한잔을 추가했을 경우의 상태를 관찰한다
                print(f"마실수 있는 음료,n={n}, k={k} ")
                newCoffee=[n-k-(n-k-status[n-k][-1][0]),status[n-k][-1][1]+1]#k=1번째 커피를 마신다면?
                #현재 용량 - 마실 커피의 용량 - (앞에식의 잔여량 안에서 비울수 있는 최대치=status[n-k][-1])
                if newCoffee[0]<=status[n-1][-1][0]:
                    if newCoffee[1]<=status[n-1][-1][1]:
                        status_K=newCoffee
                    else:
                        status_K=status[n-1][-1]
            else:
                if n==1:
                    status_K=status_N[-1]
                else:
                    status_K=status[n-2][-1] #용량 고려시, 이 잔을 마시는 것이 불가능. 
                    print("dlrj")
        if status_K[0]<=candidate_K[0]:
            if status_K[1]<candidate_K[1]:
                candidate_K=status_K
        status_N.append(status_K)
    status.append(status_N)
    status_N.append(candidate_K)
print(status)
