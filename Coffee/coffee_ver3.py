N, K = map(int, input().split())
if K==0:
    print(0)
caffeine_vol=list(map(int, input().split()))
min_cup=101
status=[[0 for i in range(N)]]
for n in range(1,K+1):
    status_N=[]
    for k in range(len(caffeine_vol)):
        cups_taken=0
        if caffeine_vol[k]<=n:
            cups_taken+=1
            remain=n-caffeine_vol[k]
            if k==0:
                if remain==0:
                    status_N.append(cups_taken)
                else:
                    status_N.append(101)
            elif status[remain][k-1]!=101:
                cups_taken+=status[remain][k-1]
                if cups_taken<status_N[-1]:
                    status_N.append(cups_taken)
                else:status_N.append(status_N[-1])
            else:status_N.append(status_N[-1])
        elif status_N:status_N.append(status_N[-1])
        else : status_N.append(101)
        
    status.append(status_N)
if min(status[-1])==101:
    print(-1)
else: print(min(status[-1]))
#newCoffee=[n-caffeine_vol[k]-(n-caffeine_vol[k]-status[n-caffeine_vol[k]][k-1][0]),status[n-caffeine_vol[k]][k-1][1]+1]