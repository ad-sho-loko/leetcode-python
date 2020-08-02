import queue

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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

        answer = []
        q = queue.Queue()
        for i in zero:
            q.put(i)
            answer.append(i)

        while not q.empty():
            n = q.get()
            answer.append(n)
            for g in range(numCourses):
                if graph[n][g]:
                    indegree[g] -= 1
                    if indegree[g] == 0:
                        q.put(g)

        return answer

