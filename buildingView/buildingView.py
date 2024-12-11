import sys
input=sys.stdin.readline
N = int(input())
buildHight = list(map(int,input().split()))
onConcave=[]
sightMax = 0
for i in range(N):
    canSee = 0
    leftMax = 1000000001
    rightMin = -1000000001
    for j in range(i-1,-1,-1):
        slope = (buildHight[i]-buildHight[j])/(i-j)
        if slope < leftMax :
            leftMax = slope
            canSee+=1
    for k in range(i+1,N):
        slope = (buildHight[i]-buildHight[k])/(i-k)
        if slope > rightMin :
            rightMin = slope
            canSee+=1
    if canSee > sightMax : 
        sightMax = canSee
print(sightMax)


