#개노가다로 풂
# 가운데부터 토네이도 이동 반시계 방향
# x->y로 이동하면 y의 모든 모래가 흩뿌려짐 (y:토네이도 도착장소)
# 소수점 버림 알파는 남는 모래 양 기존 모래 합침
# 격자 밖으로 나간 모래 양 구하기
import sys
# 비율
pro = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, -1, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]

def turn():
    global pro
    # 반시계 방향으로 회전
    turned = [[0] * 5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            turned[i][j] = pro[j][4-i]
    return turned


# 영역 밖 모래 세기
def count_sand(sand, curr, n):
    global pro
    out = 0
    s = sand[curr[0]][curr[1]]
    rest = s
    if s == 0:
        return 0
    for i in range(5):
        for j in range(5):
            if pro[i][j] == -1:
                alpha = [i, j]
                continue
            dis = [curr[0] + i - 2, curr[1] + j - 2]  #토네이도 영역
            fly = int(s * pro[i][j])
            if 0 <= dis[0] < n and 0 <= dis[1] < n:
                # 범위안에 있는 경우
                sand[dis[0]][dis[1]] += fly
                rest -= fly
            else:
                # 범위 밖
                out += fly
                rest -= fly
    sand[curr[0]][curr[1]] = 0  # 모두 날아감
    # print(alpha)
    if ((0 > curr[0] + alpha[0] - 2 or curr[0] + alpha[0] - 2 >= n) or (0 > curr[1] + alpha[1] - 2 or curr[1] + alpha[1] - 2 >= n)):
        out += rest  #!!!!!!!!! 얘도 나가는 경우
    else:
        sand[curr[0] + alpha[0] - 2][curr[1] + alpha[1] - 2] += rest
    return out

def main():
    global pro
    out = 0  # 나간 모래양
    n = int(input())
    sand = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    curr = [n // 2, n // 2]
    # 좌,하,우,상
    move = ((0, -1), (1, 0), (0, 1), (-1, 0))
    t = 1  # 직선으로 움직이는 횟수
    move_idx = 0
    while t < n:
        # 직선으로 이동
        for _ in range(2):
            for _ in range(t):
                movement = move[move_idx % 4]
                # print(movement)
                curr = [curr[0] + movement[0], curr[1] + movement[1]]
                # curr에 있는 모래가 흩날림 !
                
                # 이동
                out += count_sand(sand, curr, n)
            pro = turn()
            move_idx += 1
        t += 1
    # # 한번 더 이동해야함 t -= 1
    movement = move[move_idx % 4]
    for _ in range(t-1):
        curr = [curr[0] + movement[0], curr[1] + movement[1]]
        out += count_sand(sand, curr, n)
    print(out)



main()
