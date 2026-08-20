class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prerequisities, where a -> b
        # total of num courses we are required to take, labled frrom 0 to numCourses - 1
        # return true if it is possible to finish all courses, otherwise false

        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque(i for i in range(numCourses) if indegree[i] == 0)

        courses = 0

        while q:
            node = q.popleft()

            for nbr in graph[node]:
                indegree[nbr] -= 1

                if indegree[nbr] == 0:
                    q.append(nbr)

            courses += 1
        

        return courses == numCourses