class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        dist = {i: float("inf") for i in range(n)}
        adj = defaultdict(list) # src: dst, wt

        for u, v, w in edges:
            adj[u].append((v, w))

        heap = [(0, src)]

        while heap:
            wt, node = heapq.heappop(heap)

            if wt > dist[node]:
                continue

            dist[node] = wt

            for nbr, cost in adj[node]:
                newDist = wt + cost
                if newDist > dist[nbr]: continue

                dist[nbr] = newDist
                heapq.heappush(heap, (newDist, nbr))

        for node, dst in dist.items():
            if dst == float("inf"): 
                dist[node] = -1

        return dist