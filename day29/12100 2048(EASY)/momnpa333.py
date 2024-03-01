from collections import deque

N=int(input())
blocks=[list(map(int,input().split(' ')))for _ in range(N)]

R=0; D=1; L=2; U=3
answer=0
def move_R(blocks,N):
    newblocks=[]
    for row in blocks:
        newblocks.append(makerow(row[::-1],N)[::-1])
    return newblocks

def move_L(blocks,N):
    newblocks=[]
    for row in blocks:
        newblocks.append(makerow(row,N))
    return newblocks

def move_U(blocks,N):
    newblocks=[]
    tmp=list(zip(*blocks))[::-1]
    for row in tmp:
        newblocks.append(makerow(row,N))
    return [r[::-1] for r in list(zip(*newblocks))]

def move_D(blocks,N):
    newblocks=[]
    tmp=list(zip(*blocks[::-1]))
    for row in tmp:
        newblocks.append(makerow(row,N))
    return list(zip(*newblocks))[::-1]
    

def makerow(row,N):
    global answer
    tmp=[]
    for item in row:
        if item!=0:
            tmp.append(item)
    row=tmp
    newrow=[]
    if len(row)!=0:
        prev=row[0]
        row=deque(row[1:])
        while row:
            item=row.popleft()
            if prev==item:
                newrow.append(item*2)
                prev="!"
            else:
                if prev!="!":
                    newrow.append(prev)
                prev=item
        else:
            if prev!="!":
                newrow.append(prev)
    ret=newrow+[0]*(N-len(newrow))
    answer=max(answer,max(ret))
    return ret
# print(makerow([1,2,3,3],N))/

dq=deque([])
dq.append(blocks)
for i in range(5):
    for _ in range(len(dq)):
        board=dq.popleft()
        dq.append(move_R(board,N))
        dq.append(move_L(board,N))
        dq.append(move_U(board,N))
        dq.append(move_D(board,N))
    
print(answer)








# def bfs():
#     dq=deque([])

#     while dq:


#9:11