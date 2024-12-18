import sys
input = sys.stdin.readline

s, N , K, R1, R2, C1, C2 = map(int,input().split())
# answer = [[0 for i in range(C2-C1+1)]for j in range(R2-R1+1)]
# for time in range(s):
    # n초의 도장상태 확인. 1일 때 경우 k*k의 형태로 N칸마다 반복된다. 
    # 2의 경우라면, (N*K)^2의 형태로 N*N칸마다 반복된다. 
    # 이 생각을 하다 보니 떠오른건.. 그냥 애초에 정답 칸을 생성할때 n개의 로직을 각 칸에다가 후려버리면 안되나??
    #순서상으로는 매 칸 검사하는게 번거로워보일지 몰라도 결국에는 n개의 로직을 다 매 칸에 때려버릴게 아닌가??
    # 생성할때 C와 R의 번호도 부여해서 생성하는게 더 편해보인다.  
# test=[]
# for i in range(R2-R1+1):
for i in range(R1,R2+1):
    innerLine=[]
    # for j in range(C2-C1+1):
    for j in range(C1,C2+1):
        
        curCordinate = [i,j]
        ink=0
        for n in range(1,s+1):
            #n 초일때 경우는 (N^n)의 나머지로 나눠서 (N^n +_ n*K*N/2의 사이즈 안에 포함되는지 확인)
            subFractalCord = [curCordinate[0]%(N**n),curCordinate[1]%(N**n)]
            # 한칸 안에서 좌표안에서 K*K 안에 포함되는지 확인
            if K%2 == 1:
                steps=(N**(n-1)*K//2)
            else: steps = (N**(n-1)*K//2)-1
            if (subFractalCord[0]<= (N**n//2) + steps) and (subFractalCord[0]>= (N**n//2) - (N**(n-1)*K//2)) and (subFractalCord[1]<= (N**n//2) + steps) and (subFractalCord[1]>= (N**n//2) - (N**(n-1)*K//2)):
                # print("range", (N**n//2) + (N**(n-1)*K//2),(N**(n-1)*K//2))
                ink=1
        innerLine.append(ink)
    # test.append(innerLine)
    print(''.join(map(str,(innerLine))))
# print(test)
                

