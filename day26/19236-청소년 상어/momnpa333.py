#3:14
#  청소년 상어는 (0, 0)에 있는 물고기를 먹고, (0, 0)에 들어가게 된다. 
# 상어의 방향은 (0, 0)에 있던 물고기의 방향과 같다.
# 이후 물고기가 이동한다.

# 물고기는 번호가 작은 물고기부터 순서대로 이동한다. 
# 물고기는 한 칸을 이동할 수 있고, 이동할 수 있는 칸은 빈 칸과 다른 물고기가 있는 칸,
# 이동할 수 없는 칸은 상어가 있거나, 공간의 경계를 넘는 칸이다.
#  각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 방향을 45도 반시계 회전시킨다.
# 만약, 이동할 수 있는 칸이 없으면 이동을 하지 않는다. 그 외의 경우에는 그 칸으로 이동을 한다.
#  물고기가 다른 물고기가 있는 칸으로 이동할 때는 서로의 위치를 바꾸는 방식으로 이동한다.

# 물고기의 이동이 모두 끝나면 상어가 이동한다. 상어는 방향에 있는 칸으로 이동할 수 있는데, 한 번에 여러 개의 칸을 이동할 수 있다.
#  상어가 물고기가 있는 칸으로 이동했다면, 그 칸에 있는 물고기를 먹고, 그 물고기의 방향을 가지게 된다.

#  이동하는 중에 지나가는 칸에 있는 물고기는 먹지 않는다. 물고기가 없는 칸으로는 이동할 수 없다. 
# 상어가 이동할 수 있는 칸이 없으면 공간에서 벗어나 집으로 간다. 상어가 이동한 후에는 다시 물고기가 이동하며, 이후 이 과정이 계속해서 반복된다.

# 1. 상어가 0,0 에 들어감
# 2. 물고기 이동
# 3. 상어가 이동할수 있는 경우의수 dq에 넣기
# 4. 각 경우의수 따로 물고기 이동
# 5. 물고기 번호의 합의 최대값 구하기

# 1. bfs 구현
# 2. 물고기 이동 구현
# 3. 상어가 이동 가능한 것 구현
import copy
from collections import deque

sea=[[[] for _ in range(4)] for _ in range(4)]  

dirary=[(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
fishary={i+1:False for i in range(16)}
def moveFish(ary,fish,sharkposi):
    ary=copy.deepcopy(ary)
    fish=copy.deepcopy(fish)

    for i in fish:
        if fish[i]!=False:
            r=fish[i][0]; c=fish[i][1]; dir=fish[i][2]
            R,C=dirary[dir]
            R+=r; C+=c
            for _ in range(8):
                if 0<=R<4 and 0<=C<4 and (R,C) != sharkposi:
                    ary[R][C],ary[r][c]=ary[r][c],ary[R][C]
                    fish[i]=[R,C,dir]
                    if ary[r][c]!=False:
                        fish[ary[r][c][0]]=[r,c,ary[r][c][1]]
                    break
                dir=(dir+1)%8
                ary[r][c][1]=dir
                fish[i][2]=dir
                R,C=dirary[dir]
                R+=r; C+=c
    return ary,fish

for i in range(4):
    a1,a2,b1,b2,c1,c2,d1,d2=map(int,input().split(" "))
    sea[i][0]=[a1,a2-1]; sea[i][1]=[b1,b2-1]; sea[i][2]=[c1,c2-1]; sea[i][3]=[d1,d2-1]
    fishary[a1]=[i,0,a2-1]; fishary[b1]=[i,1,b2-1]; fishary[c1]=[i,2,c2-1]; fishary[d1]=[i,3,d2-1]


dq=deque([])
point=0
point+=sea[0][0][0]
dir=sea[0][0][1]
fishary[sea[0][0][0]]=False; sea[0][0]=False
newAry,newFish=moveFish(sea,fishary,(0,0))
dq.append([0,0,dir,newAry,newFish,point])

while dq:
    for _ in range(len(dq)):
        sharkR,sharkC,sharkDir,ary,fish,P=dq.popleft()
        R=sharkR
        for i in range(1,5):
            if 0<=sharkR+dirary[sharkDir][0]*i<4 and 0<=sharkC+dirary[sharkDir][1]*i<4:
                R=sharkR+dirary[sharkDir][0]*i;C=sharkC+dirary[sharkDir][1]*i
                if ary[R][C]!=False:
                    point=max(point,P+ary[R][C][0])
                    aryCopy=copy.deepcopy(ary); fishCopy=copy.deepcopy(fish)
                    fishCopy[aryCopy[R][C][0]]=False; aryCopy[R][C]=False
                    newAry,newFish=moveFish(aryCopy,fishCopy,(R,C))
                    dq.append([R,C,ary[R][C][1],newAry,newFish,P+ary[R][C][0]])
print(point)



