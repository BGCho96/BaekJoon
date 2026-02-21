import sys
input = sys.stdin.readline
N = int(input())
a, b, c, d, e, f = map(int,input().split())
# print(a, b, c, d, e, f)
threeMin = min([a+b+c, a+b+d, a+d+e, a+c+e, f+b+c, f+b+d, f+d+e, f+c+e])
twoMin = min([a+b, a+c, a+d, a+e,f+b, f+c, f+d, f+e, b+c, c+e, e+d, d+b])
oneMin = min([a, b, c, d, e, f])
answer = threeMin*4 + twoMin*((N-2)*4+(N-1)*4) + oneMin*((N-2)**2+((N-1)*(N-2))*4)
fiveMin = a+b+c+d+e+f - max([a,b,c,d,e,f])
if N ==1:
    answer = fiveMin
print(answer)