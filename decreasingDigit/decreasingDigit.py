def digitCombination(l,r):
    answer=1
    div = 0
    firstDigit = 0
    for i in range(r):
        div+=1
        if firstDigit:
            answer*=l-1
        else: answer*=l
        l = l - 1
        answer/=div
    return answer
def trueCombination(l,r):
    answer=1
    div = 0
    firstDigit = 0
    for i in range(r):
        div+=1
        answer*=l
        l = l - 1
        answer/=div
    return answer
N = int(input())

answerSack=[]
digit = 0
for i in range(1,12):
    digit+=1
    combination = digitCombination(10,i)
    # print(N, combination)
    if N >= combination:
        N -= combination
    else:break
# print(N)
# digit-=1
maxDigitStart = digit-1
firstDigit = 1
answer=0
if digit >= 11:
    digit = 0 
    answer=-1
if int(N) == 0:
    # if digit == 9:
    #     digit+=1
    for i in range(int(digit)-1,-1,-1):
                answerSack.append(i)
    # print(''.join(map(str,answerSack)))
    digit = 0

while digit:
    #Digit 자릿수가 있는 것은 자명. 제일 큰 자릿수는 1, 나머지는 0부터 늘려가며 좁히기.
    # if firstDigit:
    #     combination = digitCombination(maxDigitStart+1,digit)
    # else:
    combination = trueCombination(maxDigitStart+1,digit)
    if combination <= N : # 조합 부족, 더 큰 수 시도
        maxDigitStart+=1
        if maxDigitStart>9:
            answer=-1
            break
    else: # 이 수가 맞음. 고정시키고 아랫자리로 이동
        
        # subCombination = trueCombination(maxDigitStart,digit)
        if answerSack and (maxDigitStart == answerSack[-1]): # 올리는 경우...?
            answerSack[-1]+=1
            maxDigitStart=0
        answerSack.append(maxDigitStart)
        firstDigit = 0
        
        subCombination = trueCombination(maxDigitStart,digit)
        digit-=1
        N-=subCombination
        maxDigitStart = 0
        

    


        
        
        
# print(answerSack)
if answer == 0:
    print(''.join(map(str,answerSack)))
else: print(answer)

    

