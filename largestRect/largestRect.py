
import sys
input = sys.stdin.readline
while 1:
    N, M  = map(int,input().split())
    
    if N == 0 and M ==0:
        break
    matrix = []
    for i in range(N):
        temp= list(map(int,input().split()))
        matrix.append(temp)
    addUp = [0] * (M+1)
    maxArea = 0
    for newRow in matrix:
        for newRowIndex  in range(len(newRow)):
            newRowInt = newRow[newRowIndex]
            if newRowInt == 0 :
                addUp[newRowIndex] = 0
            else: addUp[newRowIndex]+=newRowInt
        stack = [-1]
        answer = 0
        for histIndex in range(M+1):
            while stack and addUp[stack[-1]]>addUp[histIndex]:
                index = stack.pop()
                h = addUp[index]
                maxArea = max(maxArea,(histIndex-stack[-1]-1)*h)
            stack.append(histIndex)
        # for i in range(M + 1):
        #     while stack and addUp[stack[-1]] > addUp[i]:
        #         height = addUp[stack.pop()]
        #         width = i - stack[-1] - 1
        #         maxArea = max(maxArea, height * width)
        #     stack.append(i)

    print(maxArea)



