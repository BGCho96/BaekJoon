import sys
input = sys.stdin.readline
C, P = map(int,input().split())
price = [[-1 for i in range(C+1)]for j in range(P)]
for i in range(P):
    curPrice = list(map(int,input().split()))
    curPrice.insert(0,0)
    for j in range(C+1):
        if i == 0 :
            if j == 0:
                price[i][j] = 0
            else:
                price[i][j] = (curPrice[j])
        elif j == 0 :
            price[i][j] = 0
        else:
            maxSack = []
            for k in range(j+1):
                if k ==0:
                    maxSack.append(price[i-1][j-k]+0)
                else:maxSack.append(price[i-1][j-k]+(curPrice[k]))
            price[i][j] = max(maxSack)
        
        
print(max(price[-1]))
        