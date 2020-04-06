import queue

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = [[-1 for _ in range(N)] for _ in range(N)]
        visited = [-1 for _ in range(N)]

        for t in times:
            graph[t[0] - 1][t[1] - 1] = t[2]

        q = queue.Queue()
        q.put((0, K - 1))

        while not q.empty():
            cost, now = q.get()

            if visited[now] != -1:
                visited[now] = min(cost, visited[now])
            else:
                visited[now] = cost

            for i, v in enumerate(graph[now]):
                if v != -1 and (visited[i] == -1 or visited[i] > cost + v):
                    q.put((cost + v, i))

        for v in visited:
            if v == -1:
                return -1

        return max(visited)
