import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
costMatrix = [[ 0 if i==j else float('inf')for i in range(N)]for j in range(N)]
for routNo in range(M):
    start, end, cost = map(int,input().split())
    startIndex = start-1
    endIndex = end -1
    costMatrix[startIndex][endIndex] = min(cost,costMatrix[startIndex][endIndex])
    

for middleCities in range(N):
        for startCities in range(N):
            for endCities in range(N):
                costMatrix[startCities][endCities] = min(costMatrix[startCities][endCities], costMatrix[startCities][middleCities]+costMatrix[middleCities][endCities])
for aaa in costMatrix:
    aaa.replace(float('inf'),'0')
    print(' '. join(list(map(str,aaa))))
