class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0] * n

        for a, b in edges:
            graph[a].append(b)
            indegree[b] += 1

        q = deque(i for i in range(n) if indegree[i] == 0)

        res = [] # ordering

        while q:
            node = q.popleft()
            
            for nbr in graph[node]:
                indegree[nbr] -= 1

                if not indegree[nbr]:
                    q.append(nbr)

            res.append(node)


        print(len(res), n)
        return res if len(res) == n else []