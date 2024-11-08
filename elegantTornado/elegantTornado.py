rowLefttop, colLefttop, rowRightdown, colRightdown = map(int,input().split())
printString=[]
maxInt=0
for j in range(rowLefttop,rowRightdown+1):
    printBag=[]
    for i in range(colLefttop,colRightdown+1):
        
        if abs(i)<-j:
            number=(2*abs(j)+1)**2-(2*abs(j))-4*abs(j)-i-j
            # printString.append('up')
        elif abs(i)<j:
            number=(2*abs(j)+1)**2-(2*abs(j))+i+j
            # printString.append('dn')
        elif abs(j)<-i:
            number=(2*abs(i))**2+1+j-i
            # printString.append('lf')
        elif abs(j)<i:
            number=(2*abs(i)+1)**2-(2*abs(i))-4*abs(i)-j-i
            if i==j+1:
                number=number=(2*abs(i-1)+1)**2+1
            # printString.append('rt')
        else:
            if i==j:#right down
                number=(2*abs(i)+1)**2
                if i<0:#left up
                    number=(2*abs(i))**2+1
            else:
                #right up
                number=(2*abs(i)+1)**2-(2*abs(i))-4*abs(i)
                if j>i:#left down
                    number=(2*abs(i)+1)**2-(2*abs(i))
        if maxInt<number:
            maxInt=number
        printBag.append(str(number))
    printString.append(printBag)

for i in printString:
    padded_list = [s.rjust(len(str(maxInt))) for s in i]
    print(' '.join(padded_list))