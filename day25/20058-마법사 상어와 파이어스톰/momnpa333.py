# 18:40
# 19:47

# 1. 회전하기
# 2. 회전후 배열 합치기
# 3. bfs로 개수확인
from collections import deque

N,Q=map(int,input().split(" "))
ary=[list(map(int,input().split(" "))) for _ in range(2**N)]
L=list(map(int,input().split(" ")))

def meltIce(ary):
    L=len(ary)
    meltary=[]
    for i in range(L):
        for j in range(L):
            cnt=0
            for r,c in ((0,1),(1,0),(0,-1),(-1,0)):
                R=i+r; C=j+c
                if 0<=R<L and 0<=C<L:
                    if ary[R][C]>0:
                        cnt+=1
            if cnt<3:
                meltary.append((i,j))
    for melt in meltary:
        r,c=melt
        ary[r][c]=max(ary[r][c]-1,0)
    return ary

def bfs(r,c,check,ary):
    dq=deque([])
    dq.append((r,c))
    check[r][c]=True
    ret=1
    while dq:
        for _ in range(len(dq)):
            r,c=dq.popleft()
            for R,C in ((0,1),(1,0),(0,-1),(-1,0)):
                curr=r+R; curc=c+C
                if 0<=curr<len(check) and 0<=curc<len(check) and check[curr][curc]==False and ary[curr][curc]>0:
                    check[curr][curc]=True
                    dq.append((curr,curc))
                    ret+=1
    return ret
            

for l in L:
    newary=[]
    for i in range(0,2**N,2**l):
        subitem=[]
        subary=[]
        for idx, item in enumerate(zip(*ary[i:i+2**l])):
            subitem.append(list(item)[::-1])
            if idx%(2**l)==2**l-1:
                subary.append(subitem)
                subitem=[]    
        newrow=[]
        for row in zip(*subary):
            print(row)
            for r in row:
                newrow+=r
            newary.append(newrow)
            newrow=[]
    ary=(meltIce(newary))

icesum=0
for row in ary:
    icesum+=sum(row)
print(icesum)

num=0
check=[[False]*len(ary) for _ in range(len(ary))]
for i in range(len(ary)):
    for j in range(len(ary)):
        if newary[i][j]>0 and check[i][j]==False:
            num=max(bfs(i,j,check,ary),num)
print(num)



    
                
