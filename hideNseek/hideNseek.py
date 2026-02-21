import sys
input = sys.stdin.readline
def findNext(x):
    x_plus = x + 1
    x_minus = x - 1
    return [x_plus, x_minus]
def doubleAble(x,k):
    while x%2 == 0 or x == k:
        if x == k :
            return True
        else:
            x/=2
    return False
def doubles(x, k):
    doublesSack =[x]
    while x*2 <= k and x != 0:
        x*=2
        doublesSack.append(x)
    return doublesSack
N, K = map(int, input().split())
# print(doubleAble(92, 23))
# print(N,K)
timeOfArrival = [-1 for i in range(max(K,N)+1)]
time = 0
arrived = set(doubles(N,K))
for i in arrived :
    timeOfArrival[i] = time
while timeOfArrival[K] == -1 :
    time += 1
    new_arrived =set()
    for i in arrived:
        if i-1>=0 and i-1<len(timeOfArrival):
            new_arrived.add(i-1)
        if i+1>=0 and i+1<len(timeOfArrival):
            new_arrived.add(i+1)
    doubleArribe = set()
    for i in new_arrived :
        doubleArribe.update(doubles(i, K))
    for updates in doubleArribe:
        if updates>=0:

            if timeOfArrival[updates] == -1:
                timeOfArrival[updates] = time
    arrived =   doubleArribe
print(timeOfArrival[-1])