import math
N, M = map(int,input().split())
answer=-1
numbers=[i for i in range(0,N*M)]
box=[]
# print(numbers)
for n in range(N):
    rows=list(map(int,input()))
    box.append(rows)
while numbers:
    startPoint=numbers.pop(0)
    if math.sqrt(box[0][0])%1 == 0 and box[0][0] > answer :
        answer = box[0][0]
    for endpoint in numbers:
        startX = startPoint//M
        startY = startPoint%M
        endX = endpoint//M
        endY = endpoint%M
        if startX == endX :
            numList=box[startX][startY:endY+1]
        else:
            m = (startY - endY)/(startX - endX)
            numList = []
            increment = 0
            for x in range(startX,endX+1):
                if (startY + m*increment) % 1 == 0 and (startY + m*increment)<M:
                    numList.append(box[x][int(startY + m*increment)])
                increment+=1
        # print(numList)
        inverseNumList=list(reversed(numList))
        for i in range(1,len(numList)):
            if (len(numList)-1)%i == 0 :
                test = int(''.join(map(str,(numList[::i]))))
                if math.sqrt(test)%1 == 0 and test > answer :
                    answer = test
                inverseTest = int(''.join(map(str,(inverseNumList[::i]))))
                if math.sqrt(inverseTest)%1 == 0 and inverseTest > answer :
                    answer = inverseTest
                if math.sqrt(numList[0])%1 == 0 and numList[0] > answer :
                    answer = numList[0]
print(answer)
