N, M = map(int,input().split())
statusCount = dict()
for n in range(N):
    tempStatus = input()
    if tempStatus in statusCount.keys():
        statusCount[tempStatus]+=1
    else:statusCount[tempStatus]=1
clicks = int(input())
maxOn = 0 
for status in statusCount.keys():
    needOn = status.count('0')
    if needOn <= clicks and (clicks-needOn)%2 == 0 and statusCount[status]>maxOn:
        maxOn = statusCount[status]
print(maxOn)
