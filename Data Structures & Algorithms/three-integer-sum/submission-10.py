class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # return ALL triplets where sum == 0
        # i, j, k are distinct
        # output should not contain any duplicate triplets

        # nums[i] can be very big and small, so no searching through solution space
        # nums is guaranteed to have at least 3 elements

        # the brute force method would be
        # anchoring i, and doing two sum on j and k
        
        # lets just code up the brute force first

        # how do you take care of duplicates?
        # maybe we can take care of them with a set?
        # maybe we can sort every triplet and keep them in a set?
        # there should be a better way
        # the time complexity is O(n^2)

        nums.sort()
        res = []
        prev = None
        for i in range(len(nums)):
            if nums[i] == prev: continue
            prev = nums[i]
            target = -nums[i]

            L, R = i + 1, len(nums) - 1

            while L < R and L < len(nums) - 1:
                if nums[L] + nums[R] == target:
                    res.append([nums[i], nums[L], nums[R]])
                    val = nums[L]
                    while nums[L] == val and L < R: L += 1
                elif nums[L] + nums[R] < target:
                    L += 1
                else:
                    R -= 1


        return res