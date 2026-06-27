class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # each row in matrix is sorted in non-decreasing order
        # the first integer of every row is greater than the last integer of the previous row
        # can you write a solution that runs in O(log(m * n)) time?
        # thats basically two binary searches

        # you do binary search on m: the start of the lists
        # and when you find a list that fits the criteria, you binary search that list

        # there are no exact matches: its about trying to find whether its smaller or not
        
        L, R = 0, len(matrix) - 1
        while L <= R:
            mid = (L + R) // 2
            if target >= matrix[mid][0]:
                L = mid + 1
            else:
                R = mid - 1

        arr = matrix[R]
        print(arr)
        L, R = 0, len(arr) - 1
        while L <= R:
            m = (L + R) // 2
            if target < arr[m]: R = m - 1
            elif target > arr[m]: L = m + 1
            else: return True

        return False
