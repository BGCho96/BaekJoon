start, end = map(int,input().split())
answer = [1] * (end - start + 1)


for i in range(2,1000001):
    sqr=i*i
    rangeStart = (start-1)//sqr
    rangeEnd = (end)//sqr
    for j in range(rangeStart,rangeEnd):
        answer[sqr*(j+1)-start]=0
print(sum(answer))


