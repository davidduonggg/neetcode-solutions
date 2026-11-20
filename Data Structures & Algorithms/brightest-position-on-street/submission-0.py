class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        numLights = defaultdict(int)
        for pos, rad in lights:
            numLights[pos - rad] += 1
            numLights[pos + rad + 1] -= 1

        max_bright = curr = 0
        res = float("-inf")

        for pos in sorted(numLights.keys()):
            curr += numLights[pos]

            if curr > max_bright:
                res = pos
                max_bright = curr

        return res

        