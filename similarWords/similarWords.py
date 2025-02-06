import sys
input = sys.stdin.readline
N = int(input())
wordList = []
for i in range(N):
    word = input().replace("\n","")
    wordList.append(word)
sortList = wordList[:]
sortList.sort()
prefixLen = 0
prefix = []
for wordIndex in range(len(sortList)-1):
    if len(sortList[wordIndex])>len(sortList[wordIndex+1]):
        longerWord = list(sortList[wordIndex])
        shorterWord = list(sortList[wordIndex+1])
    else:
        longerWord = list(sortList[wordIndex+1])
        shorterWord = list(sortList[wordIndex])
    zeroLen = 0
    for charIndex in range(len(shorterWord)):
        compare = (ord(shorterWord[charIndex])-ord(longerWord[charIndex]))
        if compare == 0:
            zeroLen+=1
            if zeroLen > prefixLen:
                prefixLen = zeroLen
                prefix = set()
                prefix.add(''.join(shorterWord[:charIndex+1]))
                # print(prefixLen,prefix)
            if zeroLen == prefixLen:
                prefix.add(''.join(shorterWord[:charIndex+1]))
        else: break


    # print(result)
# print(prefix)
count = 2
fixed = 0
fixedPrefix = ''
for word in wordList:
    if count ==0:
        break
    testString = list(word)
    if (''.join(testString[:prefixLen]) in prefix) and (fixed == 0):
        # print(''.join(testString[:prefixLen]))
        fixedPrefix = ''.join(testString[:prefixLen])
        fixed=1
    if fixed == 1:
        if ''.join(testString[:prefixLen]) == fixedPrefix:
            count-=1
            print(word)

    
