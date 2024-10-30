N= int(input())
sack=[]
for i in range(N):
    testSignal=list(map(str,list(input())))
    partDone=[]
    part=[]
    flag=0
    while testSignal:
        
        
        # print("testSignal",testSignal)
        # print('while start')
        # print('pree',testSignal[0:3],''.join(testSignal[1:3]))
        while testSignal[0:3] and ''.join(testSignal[0:2])!='10':
            part.append(testSignal.pop(0))
            # print("testSignal",testSignal)
        if ''.join(testSignal[0:3])=='101':
             part.append(testSignal.pop(0))
             partDone.append(part)
             partDone.append([testSignal.pop(0),testSignal.pop(0)])
             part=[]
        else: 
            if part:
                partDone.append(part)
                part=[]
            if testSignal:
                part.append(testSignal.pop(0))
    
    # print('check partdones',partDone,part)
    for parts in partDone:
        flag=1
        if sum(list(map(int,parts)))==1 and ''.join(parts)=='01':
            flag=0
            # print("1")
        
        if parts.count('0')>1 and parts[-1]=='1' and parts[0]=='1':
            flag=0
            # print("2")
        if flag==1:
            break
        
            
        
    # print(partDone)
    print(partDone)
    if flag==0:
        print("YES")  
    else: print("NO")
