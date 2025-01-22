import sys
input = sys.stdin.readline
answer=1
N = int(input())
priceInfo = []
for i in range(N):
    temp=list(map(int,input().strip()))
    priceInfo.append(temp)
maxPrice=151
dp = [[maxPrice for i in range(2**N)] for j in range(N)]
print(dp)
print(priceInfo)
# tradeTrace=[[1,0]]
# while tradeTrace:
#     newTrace=[]
#     for sellerInfo in tradeTrace:
#         sellerList = sellerInfo[:-1]
#         price = sellerInfo[-1]
#         lastPossess = sellerList[-1]
#         for buyer in range(1,len(priceInfo[lastPossess-1])+1):
#             newPirce = priceInfo[lastPossess-1][buyer-1]
#             if newPirce>=price and buyer not in sellerList:
#                 newList = sellerList[:]
#                 newList.append(buyer)
#                 if len(newList) > answer:
#                     answer = len(newList)
#                 newList.append(newPirce)
#                 newTrace.append(newList)
#     tradeTrace=newTrace
# print(answer)
for seller in range(N):
    for buyer in range(len(priceInfo[N-1])):
        buyerPrice = priceInfo[seller][buyer]
        hands = bin((1<<(buyer))|(1<<(seller)))
        dp[buyer][int(hands,2)] = buyerPrice
print(dp)