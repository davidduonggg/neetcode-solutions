class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return the median value among all elements of the two arrays
        # what would the brute force be?
        # merge both lists, and then run binary search on the entire array
        # is there a way we can circumvent merging both of the lists? they are both in ascending order
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)

        aL, aR = 0, len(A) - 1
        while True:
            aMid = (aL + aR) // 2
            bMid = (total // 2) - aMid - 2

            aLeft = A[aMid] if aMid >= 0 else float('-inf')
            aRight = A[aMid + 1] if aMid + 1 < len(A) else float('inf')
            bLeft = B[bMid] if bMid >= 0 else float('-inf')
            bRight = B[bMid + 1] if bMid + 1 < len(B) else float('inf')

            if aLeft <= bRight and bLeft <= aRight: # we found the correct partition
                if total % 2: return min(aRight, bRight)
                else: return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            
            else:
                if aRight > bLeft:
                    aR = aMid - 1
                else:
                    aL = aMid + 1

        return 0


        
    