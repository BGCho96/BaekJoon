#다이아몬드 수 확인을 한다. 나머지를 입력 가능한가를 따지면 된다.
import math
N= int(input())
for n in range(N):
    start, end = map(int, input().split())
    jumpDistance = end - start
    
    #first jump
    diamond = int(math.sqrt(jumpDistance))
    remain=jumpDistance-diamond**2
    # print(diamond,remain)
    extra=0
    while remain:
        for i in range(diamond,0,-1):
            extra+=remain//i
            remain=remain%i
    # print(extra)
    asnwer=diamond*2 - 1 + extra
    print(asnwer)


    