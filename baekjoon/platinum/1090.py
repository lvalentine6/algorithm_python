from itertools import product

n = int(input())
lst = [[int(x) for x in input().split()] for _ in range(n)]
x_set = set()
y_set = set()

for i in range(n):
    x_set.add(lst[i][0])
    y_set.add(lst[i][1])

comb = list(product(x_set, y_set))

answer_lst = []

for i in range(1, n + 1):
    mid_lst = []
    for c in comb:
        dis_lst = []
        for k in lst:
            dis_lst.append(abs(c[0] - k[0]) + abs(c[1] - k[1]))

        mid_lst.append(sum(sorted(dis_lst)[:i]))

    answer_lst.append(min(mid_lst))

print(*answer_lst)

# 시작시간
## 3시간

# 도움
## GPT, 강의 힌트만 얻음

# 문제 이해
## 1개의 체커가 같은칸에 모이는 최소 이동횟수 0번
## 2개의 체커가 같은칸에 모이는 최소 이동횟수 ?
## k는 1부터 시작해서 N까지

# 해결 아이디어
## 그냥 모든 조합을 구하면 시간초과가 날것으로 예상
## 중앙값 아이디어를 차용하자 주어진 x값과 y값을 따로 받아서 중앙값을 탐색하자
## 만약 모든 N개의 최소거리를 구하라면 그냥 x 중앙값, y 중앙값이 최적이지만
## 적어도 k라면 중앙값이 최적이 아닐수 있어 x,y의 모든 조합 따져봐야함
## 그래봐야 50 * 50 이기 때문에 가능함

# 계획
## 1. 전체 리스트를 받고, x,y 나누어서 set에 넣어줌
## 2. x,y 의 모든 조합 구하기
## 3. k를 1부터 N + 1까지 순회한다.
## 4. 인풋값 하나씩 순회하며 조합과의 거리를 구하고 리스트에 넣음
## 5. 리스트에서 k까지 자르고 더한후에 mid_lst에 넣음
## 6. mid_lst에서 최솟값을 answer_lst에 넣고 모든 k의 값 출력
