import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
nodes = [[] for _ in range(n)]
indegree = [0] * n
edges = []

# 간선 입력
for _ in range(m):
    u, v = map(int, input().split())
    edges.append((u, v))   # 원래 번호 저장
    u -= 1
    v -= 1
    nodes[u].append(v)
    indegree[v] += 1

# 위상정렬 (Kahn)
q = deque([i for i in range(n) if indegree[i] == 0])
queries = []
while q:
    u = q.popleft()
    for v in nodes[u]:
        queries.append((u, v))
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

# 진짜 간선만 추리기
trueQs = []
for i in range(m):
    trueness = int(input())
    if trueness:
        trueQs.append(edges[i])

# DP로 최장 경로 구하기
depths = [0] * n
trueQs = set(trueQs)  # membership test 빠르게

for u, v in queries:
    if (u+1, v+1) in trueQs:
        print(f"? {u+1} {v+1}", flush=True)
        depths[v] = max(depths[v], depths[u] + 1)

print(f"! {max(depths)}", flush=True)