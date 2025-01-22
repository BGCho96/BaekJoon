import sys
input = sys.stdin.readline
N = int(input())
membershipStandard = set()
numList = list(map(int,input().split()))
numList= sorted(numList)
# print(numList)
answer=0
for i in range(N):
    sumList = numList[:i]+numList[i+1:]
    start = 0
    end = len(sumList)-1
    while start<end:
        currentSum = sumList[start] + sumList[end]
        if currentSum == numList[i]:
            answer +=1
            break
        if currentSum < numList[i]:
            start +=1
        if currentSum > numList[i]:
            end -=1
    
print(answer)

