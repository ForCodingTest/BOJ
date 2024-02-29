# 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
# 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

# 1. 이분탐색
# 2. min 가정 적은 블록, max 가장 많은 블록
# 3. 못만들면 작은걸로 만들면 

import sys

input=sys.stdin.readline

N,M,B=map(int,input().split(' '))
board=[list(map(int,input().split(' '))) for i in range(N)]
S=0
end=0; start=float('inf')
for row in board:
    S+=sum(row)
    start=min(start,min(row))
    end=max(end,max(row))

timeary=[]

def isposi(num,B,S):
    # if num*len(board)*len(board[0])>S+B:
    #     return False
    time=0
    for row in board:
        for item in row:
            if item<num:
                B-=(num-item)
                time+=(num-item)
            elif item>num:
                B+=(item-num)
                time+=(item-num)*2
    timeary.append((time,num))

    return time
    




# def bisearch(r,l,S,B,cur):
#     if r>l:
#         return
#     mid=(r+l)//2
#     # print(mid)
#     c=isposi(mid,B,S,cur)
#     if c<cur:
#         bisearch(r,mid-1,S,B,cur)
#         isposi(mid+1,B,S,cur)
#     else:
#         bisearch(mid+1,l,S,B,cur)

# print(board,start,end)
end = min((S+B)//(M*N),end)
end= min(256,end)
# bisearch(start,end,S,B,float('inf'))
for i in range(start,end+1):
    isposi(i,B,S)

timeary=sorted(timeary,key=lambda x:(x[0],-x[1]))
print(*timeary[0])
# print(timeary)