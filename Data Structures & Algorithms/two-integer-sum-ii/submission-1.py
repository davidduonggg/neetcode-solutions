class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # non-decreasing order

        # return the indicies of two numbers that add up to a given target number
        # index1 < index2 and index1 != index2

        # solution must use O(1) additional space

        L, R = 0, len(numbers) - 1

        while L < R:
            curr = numbers[L] + numbers[R]

            if curr == target:
                return [L + 1, R + 1]
            elif curr < target:
                L += 1
            else: 
                R -= 1

        return [L + 1, R + 1]