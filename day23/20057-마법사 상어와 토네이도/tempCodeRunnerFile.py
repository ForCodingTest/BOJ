# 11:16
# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다. 토네이도는 한 번에 한 칸 이동한다. 다음은 N = 7인 경우 토네이도의 이동이다.
# y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다. 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다
import math
N=int(input())
Map=[list(map(int,input().split())) for _ in range(N)]

R,C=N//2,N//2

sand=[[0,0,0.02,0,0],[0,0.1,0.07,0.01,0],[0.05,0,0,0,0],[0,0.1,0.07,0.01,0],[0,0,0.02,0,0]]
answer=0
dist=0

def makesand(R,C,num,Amount):
    rotateSand=sand
    for _ in range(num):
        rotateSand=[i for i in zip(*rotateSand)][::-1]
    L=len(Map)
    Rc=R-2; Cc=C-2
    throwsum=0
    ret=0
    for i in range(5):
        for j in range(5):
            throwSand=int(Amount*rotateSand[i][j])
            # print(throwSand)
            throwsum+=throwSand
            if 0<=i+Rc<L and 0<=j+Cc<L:
                Map[i+Rc][j+Cc]+=throwSand
            else:
                ret+=throwSand
    dir=((0,-1),(1,0),(0,1),(-1,0))
    if 0<=R+dir[num][0]<L and 0<=C+dir[num][1]<L:
        Map[R+dir[num][0]][C+dir[num][1]]+=Amount-throwsum
    else:
        ret+=Amount-throwsum
    
    # print(ret)
    return ret
            


while True:
    for num,dir in enumerate(((0,-1),(1,0),(0,1),(-1,0))):
        if num==0:
            dist+=1
        if num==2:
            dist+=1
        # R=R+dir[0]*dist; C=C+dir[1]*dist
        
        for _ in range(dist):
            R+=dir[0]; C+=dir[1]
            # print(int(sand[R][C]*0.12))
            answer+=makesand(R,C,num,Map[R-dir[0]][C-dir[1]])
            # print(R,C)
            Map[R-dir[0]][C-dir[1]]=0
            if R==0 and C==0:
                Map[0][0]-=int(Map[0][0]*0.01)
                print(answer+Map[0][0])
                exit(0)

        if R==0 and C==0:
            break
    if R==0 and C==0:
        break
        


        

