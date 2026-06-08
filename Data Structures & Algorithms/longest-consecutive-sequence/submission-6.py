class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       # return the length of the longest consecutive
       # sequence of elements that can be formed

       # each element is exactly 1 greater than the previous element
       # elements do not have to be consecutive in the original array
       # nums i can be extremely large

       # the brute force would be to treat every single number as the start of a sequence
       # O (n^2)

       # how do i prune the set
       # how do i distinguish the start of a sequence vs middle of a sequence
        if not nums: return 0

        longest = 0
        valid = set(nums)

        for num in valid:
            if num - 1 in valid: continue

            # we found the start of a sequence
            curr = num
            while curr in valid:
                curr += 1

            longest = max(longest, curr - num)

        return longest

            