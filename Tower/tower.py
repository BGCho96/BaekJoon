import sys
import re

input = sys.stdin.readline
N = int(input())
# targetList = []
for i in range(N):
    target = int(input())
    tar_binary_only = bin(target)[2:]
    if tar_binary_only =='1':
        print('0')
        continue
    split_chunks = [chunk for chunk in re.split('0+', tar_binary_only[1:]) if chunk]
    print(len(tar_binary_only)+len(split_chunks))
    # print(re.split('0+',tar_binary_only[1:]))
    
    for j in range(len(tar_binary_only)):
        print(f'1 {j+1}')
    sub_bits = tar_binary_only[1:]
    reversed_sub = sub_bits[::-1]

    i = 0
    while i < len(reversed_sub):
        if reversed_sub[i] == '1':
            start = i + 1
            while i + 1 < len(reversed_sub) and reversed_sub[i + 1] == '1':
                i += 1
            end = i + 1
            print(f'{start+1} {end+1}')
        i += 1
    
