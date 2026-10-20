class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            temp = [0] + res[i] + [0]
            level = []
            for i in range(len(temp)-1):
                level.append(temp[i] + temp[i + 1])

            res.append(level[:])

        return res