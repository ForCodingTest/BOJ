#12:35
#1:30

N,M,K=map(int,input().split(' '))

infos=[list(map(int,input().split(' '))) for _ in range(M)]

dirset={idx:item for idx,item in enumerate(((-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)))}

def move(N):
    itemset=[]
    for row in ary:
        for item in row:
            while item:
                r,c,m,s,d=item.pop()
                newr=(r+dirset[d][0]*s)%N
                newc=(c+dirset[d][1]*s)%N
                itemset.append((newr,newc,m,s,d))
    for item in itemset:
        r,c,m,s,d=item
        ary[r][c].append(item)

def divide(items):
    ssum=0; msum=0; dir=[]
    r,c,isodd,iseven=(0,0,0,0)
    ret=[]
    for item in items:
        r,c,m,s,d=item
        ssum+=s
        msum+=m
        dir.append(d)
    if msum//5==0:
        return ret
    for di in dir:
        if di%2!=0:
            break
    else:
        iseven=True

    for di in dir:
        if di%2!=1:
            break
    else:
        isodd=True
    
    for d in range(4):
        if isodd or iseven:
            ret.append((r,c,msum//5,ssum//len(items),d*2))
        else:
            ret.append((r,c,msum//5,ssum//len(items),d*2+1))
    return ret

ary=[[[] for _ in range(N)] for _ in range(N)]

for info in infos:
    r,c,m,s,d=info
    # print(r-1,c-1)
    ary[r-1][c-1].append((r-1,c-1,m,s,d))

for _ in range(K):
    move(N)
    for r in range(N):
        for c in range(N):
            if len(ary[r][c])>1:
                ary[r][c]=divide(ary[r][c])
answer=0
# print(ary)
for row in ary:
    for items in row:
        for item in items:
            answer+=item[2]

# print(ary)
print(answer)
