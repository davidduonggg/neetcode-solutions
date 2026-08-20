class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            incoming[a] += 1

        q = deque(i for i in range(numCourses) if incoming[i] == 0)

        res = []

        while q:
            node = q.popleft()

            for nbr in graph[node]:
                incoming[nbr] -= 1

                if incoming[nbr] == 0: q.append(nbr)

            res.append(node)

        return res if len(res) == numCourses else []
