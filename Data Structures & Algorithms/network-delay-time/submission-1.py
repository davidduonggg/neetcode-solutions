class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # starting node k
        # weighted directed graph
        # (source, target, weight) for times
        # return the minimum time it takes for all n nodes to receive the signal
        # if it is impossible, return -1

        # create the adjacency list

        adj = defaultdict(list) # weight, target
        for src, tgt, wt in times:
            adj[src].append((wt, tgt))
        distances = [float("inf")] * (n + 1)
        distances[k], distances[0] = 0, 0
        minHeap = [(0,k)] 

        while minHeap:
            dist, node = heapq.heappop(minHeap)
            
            if dist > distances[node]: # if it's greater than current distance, we ignore
                continue

            for wt, nbr in adj[node]:
                new_dist = dist + wt
                if new_dist >= distances[nbr]: continue
                distances[nbr] = new_dist
                heapq.heappush(minHeap, (new_dist, nbr))


        maxTime = max(distances)
        return maxTime if maxTime != float("inf") else -1