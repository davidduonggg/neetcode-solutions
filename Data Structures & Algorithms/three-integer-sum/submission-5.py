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
        dupes = set()
        res = []

        for i in range(len(nums)):
            target = -nums[i]

            hashmap = {} # num: index
            for j in range(i + 1, len(nums)):
                b = target - nums[j]
                if b in hashmap:
                    result = [nums[i], nums[j], b]
                    result.sort()
                    if not tuple(result) in dupes:
                        res.append(result)
                        dupes.add(tuple(result))
                
                hashmap[nums[j]] = j

        return res