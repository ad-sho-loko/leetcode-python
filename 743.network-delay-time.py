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
