class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        dist = {i: float("inf") for i in range(n)}
        adj = defaultdict(list) # src: dst, wt

        for u, v, w in edges:
            adj[u].append((v, w))

        q = deque()
        q.append((src, 0))

        while q:
            node, wt = q.popleft()

            if wt > dist[node]:
                continue

            dist[node] = wt

            for nbr, cost in adj[node]:
                q.append((nbr, wt + cost))

        for node, dst in dist.items():
            if dst == float("inf"): 
                dist[node] = -1

        return dist