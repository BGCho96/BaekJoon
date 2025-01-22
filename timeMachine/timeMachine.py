import sys
input = sys.stdin.readline
numCity, numBusRoute = map(int,input().split())
busInfo = [[None for i in range(numCity)]for j in range(numCity)]
# print(numCity, numBusRoute)
for busNo in range(numBusRoute):
    start, destination, timeCost = map(int,input().split())
    if (busInfo[start-1][destination-1] is None) or timeCost<busInfo[start-1][destination-1]:
        busInfo[start-1][destination-1] = timeCost
# print(busInfo)
routeList =[[[1,i+1],busInfo[0][i]] for i in range(numCity)]
# print(routeList)
flag = 0
while routeList:
    for i in range(numCity):
        if busInfo[i][i] is not None and busInfo[i][i]<0:
            flag =1
        
    if flag:
        print(-1)
        break
    candidates=[]
    for visitList, totalCost in routeList: # 시간을 단축시킬수 있는 경로들 나열
        curCity = visitList[-1]
        for cityNo in range(numCity): #해당 경로들의 다음 후보들 나열
            timeCost = busInfo[curCity-1][cityNo]
            if ( (totalCost is not None) and (timeCost is not None))  and ((busInfo[0][cityNo] == None) or (totalCost+timeCost < busInfo[0][cityNo])): # 만약 이동 가능한 경로이면서, 경로를 이어 붙였을 때 시간이 단축된다면, 
                busInfo[0][cityNo] = totalCost+timeCost
                newList = visitList[:]
                newList.append(cityNo+1)
                for test in set(newList):
                    if newList.count(test)>3:
                        flag=1
                candidates.append([newList,totalCost+timeCost])
                
            
    if flag:
        break
    routeList = candidates
if not flag:
    for finalCost in range(1,len(busInfo[0])):
        if busInfo[0][finalCost] is None:
            print(-1)
        else:print(busInfo[0][finalCost])