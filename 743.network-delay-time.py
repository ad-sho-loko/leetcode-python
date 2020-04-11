import heapq

class Solution:
    # ダイクストラ法による解法。
    # 幅優先探索をベースとしながらも優先度付きキューを利用することで、
    # どのノードであっても初めてに訪れたときのコストが必ず最小になることを利用する。
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = [[-1 for _ in range(N)] for _ in range(N)]
        visited = [-1 for _ in range(N)]

        # 訪れたことのないノードの数を記録する変数。
        # すべてのノードを探索済みか確認するのがO(n)になることを防ぐためにある。
        remain = N

        for t in times:
            frm, to, cost = t
            graph[frm - 1][to - 1] = cost

        pq = [(0, K - 1)]
        heapq.heapify(pq)

        while pq:
            cost, now = heapq.heappop(pq)
            if visited[now] != -1:
                continue

            visited[now] = cost
            remain -= 1

            for ni, ncost in enumerate(graph[now]):
                if ncost != -1 and visited[ni] == -1:
                    heapq.heappush(pq, (ncost + cost, ni))

        if remain == 0:
            return max(visited)
        else:
            return -1

    # ベルマンフォード法による解法。
    def networkDelayTime2(self, times: List[List[int]], N: int, K: int) -> int:
        dist = [999 for _ in range(N)]
        graph = [[-1 for _ in range(N)] for _ in range(N)]
        for t in times:
            frm, to, cost = t[0]-1, t[1]-1, t[2]
            graph[frm][to] = cost

        # 開始点の距離をゼロ初期化することを忘れないこと
        dist[K-1] = 0

        for i in range(N):          # ループ
            for j in range(N):      # from
                for k in range(N):  # to
                    if j == k:
                        continue

                    cost = graph[j][k]
                    if cost != -1 and dist[k] > dist[j] + cost:
                        dist[k] = dist[j] + cost

        for d in dist:
            if d == 999:
                return -1

        return max(dist)
