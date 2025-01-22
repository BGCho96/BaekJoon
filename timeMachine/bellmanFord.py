import sys, copy
input = sys.stdin.readline
numCity, numBusRoute = map(int,input().split())
busInfo = []
# print(numCity, numBusRoute)
for busNo in range(numBusRoute):
    start, destination, timeCost = map(int,input().split())
    busInfo.append([start,destination,timeCost])
cityCost = [int(10e9) for i in range(numCity)]
cityCost[0]=0
flag=0
for i in range(1,numCity+1):
    for start, dest, timeCost in busInfo:
        if cityCost[start-1]!=int(10e9) and cityCost[dest-1]>cityCost[start-1] + timeCost:
            cityCost[dest-1] = cityCost[start-1] + timeCost
            if i==numCity:
                flag=1
if flag:
    print(-1)
else:
    for i in cityCost[1:]:
        if i == int(10e9):
            print(-1)
        else: print(i)