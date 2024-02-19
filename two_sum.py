class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            if nums[0] + nums[1] == target:
                return [0,1]
        i = 0
        j = 1
        while i < len(nums):
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
            j = i + 1
