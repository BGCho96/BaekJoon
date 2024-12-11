import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6) 
numTrial = int(input())
for i in range(numTrial):
    ruleSack = []
    
    needDict = dict()
    costDict = dict()
    numConst, numRules = map(int, input().split())
    reqNum = [0 for k in range(numConst)]
    minDone=[-1 for k in range(numConst)]
    cost = list(map(int,input().split()))
    for j in range(numRules):
        tempRule = list(map(int,input().split()))
        if tempRule[0] in needDict.keys():
            needDict[tempRule[0]].append(tempRule[1])
            reqNum[tempRule[1]-1]+=1
        else:
            needDict[tempRule[0]] = [tempRule[1]]
            reqNum[tempRule[1]-1]+=1

        if tempRule[1] in costDict.keys():
            costDict[tempRule[1]].append(tempRule[0])
        else:
            costDict[tempRule[1]] = [tempRule[0]]
            
    winConst = int(input())

    while 1:
        constAble = []
        for k in range(len(reqNum)) :
            if reqNum[k] == 0 :
                if k+1 in needDict.keys():
                    constAble.extend(needDict[k+1])
                    reqNum[k]-=1
                if k+1 in costDict.keys():
                    cands=[]
                    reqBuilds = costDict[k+1]
                    for rB in reqBuilds:
                        cands.append(minDone[rB-1])
                    minDone[k]=max(cands)+cost[k]
                else: minDone[k] = cost[k]
        

        for release in constAble:
            reqNum[release-1]-=1
        if minDone[winConst-1] != -1:
            break
    print(minDone[winConst-1])
            