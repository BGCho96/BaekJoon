def solution(a):
    answer = -1
    newA = [a[0]]
    for i in range(1,len(a)-1):
        if a[i-1]==a[i] and a[i]==a[i+1]:
            continue
        else:newA.append(a[i])
    newA.append(a[-1])
    # print(newA)
    # for i in range(len(a)):
        
    cands = set(newA)
    indexDict=dict()
    if len(a) ==1:
        return 0
    elif len(cands)==len(a):
        return 2
    for candsStr in cands:
        indexDict[candsStr]=[]
    for i in range(len(newA)):
        indexDict[newA[i]].append(i)
    # print(indexDict)
    indexOrder=sorted(indexDict.items(), key = lambda x:len(x[1]),reverse=True)
    # print(indexOrder)
    for testIndex1 in indexOrder:
        # print(testIndex1[1])
        testIndex=testIndex1[1]
        count=0
        temp = [ i for i in range(len(newA)) if i not in testIndex]
        if min(len(temp)*2,len(testIndex)*2)<=answer:
            break
        #왼쪽확인 후 오른쪽 확인
        for indexCands in testIndex:
            if indexCands-1 in temp:
                temp.remove(indexCands-1)
                count+=1
            elif indexCands+1 in temp:
                temp.remove(indexCands+1)
                count+=1
        answer=max(answer, count*2)
        # print(count)
    
    return answer