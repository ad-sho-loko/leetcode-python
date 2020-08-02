import queue

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[False for _ in range(numCourses)] for _ in range(numCourses)]
        for pre in prerequisites:
            to = pre[0]
            frm = pre[1]
            graph[frm][to] = True

        zero = []
        indegree = [0] * numCourses
        for i in range(numCourses):
            for j in range(numCourses):
                if graph[j][i]:
                    indegree[i] += 1

            if indegree[i] == 0:
                zero.append(i)

        if len(zero) == 0:
            return False

        q = queue.Queue()
        for i in zero:
            q.put(i)

        count = 0
        while not q.empty():
            n = q.get()
            count += 1
            for g in range(numCourses):
                if graph[n][g]:
                    indegree[g] -= 1
                    if indegree[g] == 0:
                        q.put(g)

        return count == numCourses
