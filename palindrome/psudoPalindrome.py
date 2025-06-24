'''
1. 문자가 같아서 넘어가는 경우.
2. 둘중 한쪽만 삭제의 여지가 확실한 경우(오른쪽은 지워도 유사로 넘어가지만, 왼쪽은 되지 않는 등)
3. 둘다 애매해서, 한글자를 더 봐야 하는 경우.
4. 2번에서 이미 유사 회문 이력이 있을 경우 - 그냥 break
'''
import sys
# input = sys.stdin.readline
N = int(input())
for n in range(N):
    word = input()
    startP = 0
    endP = len(word)-1
    answer = 0
    if word == word[::-1]:
        pass
    else:
        while startP<=endP: 
            if word[startP] == word[endP]:
                startP+=1
                endP-=1
            else:
                rightWord  =word[:endP]+word[endP+1:]
                leftWord  =word[:startP]+word[startP+1:]
                if leftWord == leftWord[::-1] or rightWord == rightWord[::-1]:
                    answer = 1
                else:
                    answer = 2
                
                break
    print(answer)

            
    