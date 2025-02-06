'''
원래의 수열을 어떻게 제거하여, 스타수열로 만들어낼 것이냐 의 문제이다. 
스타수열의 커다란 조건 2개는,
2개의 연속 요소는 다른 숫자일 것이며, 이것들이 모두 하나 이상의 교집합 원소를 가질 것. 
가장 먼저 떠오르는 직관적인 식별인자는 : 
1. 1칸 이상 떨어져있으면서 같은 요소의 숫자. Ex) a, 1, 1, a, 2, 3,  a, 4, a, 1, a
반례를 깊이 고민하지 않았을 시, 그냥 a를 무조건 많이 세버리면 그만 아닌가? 붙어있는 a는 그냥 1개의 a로 치고 말이다. 
근데 이러면 1,a,a,2와 같은 경우를 놓치게 된다. 3개 이상의 동일문자는 2개의 동일문자로 치환 가능하겠지만, 2개의 경우는 고려를 해야한다. 약간의 dp를 떠올리게 한다. 도둑질 문제인가 앞선 집을 털까 말까 결정하는 그 문제 말이다. 

그렇다면 붙어있는 2개의 문자 중 하나를 버리는 것이 이득이 되는 케이스가 있는지를 확인하면 되는거 아닌가??
a ,4 a, a, 5 a ,6 a ,a 7 ,a
a ,4 a ,a 5, a 6 ,a, a 7, a
a 4 a a 5 a 6 a a 7 a

지금의 얕은 예측으로는 답은 No이다. 연속된 교집합 요소에서 욕심을 부려봤자 1개의 다른 요소 손해를 입힐 뿐이다. 
그럼 이제 골때리는 문제는 2개의 교집합 후보가 동률일 때다. 어떤놈은 손해를 발생시키고, 어떤놈은 발생시키지 않을 것이다. 
어느놈인지 내가 어떻게 알 수 있을까??
답은 쉴 틈을 주는놈인가 여지인거 같다. 2개의 연속 교집합 요소가 2번 연속 등장 할 때, 
aa 1 2 a 3 a 4 5 aa
이런 식일 때, 다른 요소가 2번 연속 등장하는애가 있다면 밀어줄 수 있다. 
근데 골때리게 길이가 50만이다. 이쯤되면 1번 순회에 뭔가 특정 변수를 입력 받아서 갱신형으로 가야하나 싶은데....
어렵다. 
O(n) - 3개 이상 중복 제거 + 각 요소의 갯수 측정
등장 가능한 최대 공통집합문자 - n개
여기서 n개의 모든 문자후보에 대해서 잉여 문자 존재여부를 조사하면 재수없으면O(n^2)이 최악의 경우 발생해버린다. 
차라리 모든 문자를 읽으면서, 
딕셔너리를 하나 완성하는게 빠를 지경이다. 
일단 후자를 시도해보고, 안되면 답을 보자. 
후자를 했는데 안됐는데 힌트가 그리디다....후....

'''
def solution(a):
    answer = -1
    candidates= set(a)
    if len(a) ==1:
        return 0
    elif len(candidates)==len(a):
        return 2
    candidateScore=dict()
    for cands in candidates:
        candidateScore[cands] = 0
    
    # print(candidateScore)
    for curStr in a:
        # print('입력문자',curStr)
        for curAll in candidateScore.keys():
            if curAll!=curStr and candidateScore[curAll]%1 == 0:
                candidateScore[curAll]+=0.25
                # print('잉여문자 입력으로 인한 부분 가점',curAll)
            elif curAll==curStr and candidateScore[curAll]%1 == 0:
                candidateScore[curAll]+=0.75
                # print('후보문자 입력으로 인한 부분 가점',curAll)
            elif curAll!=curStr and candidateScore[curAll]%1 == 0.75:
                candidateScore[curAll]+=0.25
                # print('후보문자 대기로 인한 부분 가점',curAll)
            
            
        
        if candidateScore[curStr]%1 == 0.25: # 잉여문자가 대기중이라면 완성
            candidateScore[curStr]+=0.75
            # print('잉여문자 대기로 인한 가점',curStr)
            
        # print(candidateScore)
    # print(candidateScore)
    for i in candidateScore.keys():
        answer = max ( candidateScore[i], answer)
    return (answer//1)*2